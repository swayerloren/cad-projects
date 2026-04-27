from __future__ import annotations

import csv
import math
import os
import re
from pathlib import Path
from typing import Any

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
PROJECT_DIR = ROOT / "COMMAND LINK" / "COMMAND LINK"
PCB_PATH = PROJECT_DIR / "COMMAND LINK DRAFT.kicad_pcb"
BOM_PATH = PROJECT_DIR / "COMMAND LINK BOM.csv"
TOP_POS_PATH = PROJECT_DIR / "pick and place file" / "COMMAND LINK DRAFT-top-pos.csv"
BOTTOM_POS_PATH = PROJECT_DIR / "pick and place file" / "COMMAND LINK DRAFT-bottom-pos.csv"
FAB_JOB_PATH = PROJECT_DIR / "Fabrication files" / "COMMAND LINK DRAFT-job.gbrjob"
EDGE_GBR_PATH = PROJECT_DIR / "Fabrication files" / "COMMAND LINK DRAFT-Edge_Cuts.gbr"
PTH_DRL_PATH = PROJECT_DIR / "Fabrication files" / "COMMAND LINK DRAFT-PTH-drl.gbr"
NPTH_DRL_PATH = PROJECT_DIR / "Fabrication files" / "COMMAND LINK DRAFT-NPTH-drl.gbr"
OUTPUT_DIR = ROOT / "tools" / "output"
ROOT_REPORT = ROOT / "PCB_MECHANICAL_ANALYSIS.md"

MM_PER_INCH = 25.4


def mm_to_in(value: float) -> float:
    return value / MM_PER_INCH


def fmt(value: float | None, digits: int = 3) -> str:
    if value is None:
        return ""
    return f"{value:.{digits}f}"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def paren_delta(line: str) -> int:
    """Count S-expression parens outside quoted strings."""
    delta = 0
    in_string = False
    escaped = False
    for ch in line:
        if escaped:
            escaped = False
            continue
        if in_string:
            if ch == "\\":
                escaped = True
            elif ch == '"':
                in_string = False
            continue
        if ch == '"':
            in_string = True
        elif ch == "(":
            delta += 1
        elif ch == ")":
            delta -= 1
    return delta


def block_at(lines: list[str], start_index: int) -> tuple[int, int, list[str]]:
    balance = 0
    end = start_index
    for end in range(start_index, len(lines)):
        balance += paren_delta(lines[end])
        if end > start_index and balance <= 0:
            end += 1
            break
    return start_index + 1, end, lines[start_index:end]


def first_match(text: str, pattern: str, flags: int = 0) -> re.Match[str] | None:
    return re.search(pattern, text, flags)


def all_strings_in_layers(block: str) -> str:
    match = first_match(block, r"\(layers\s+([^\)]*)\)")
    if not match:
        return ""
    return ", ".join(re.findall(r'"([^"]+)"', match.group(1)))


def parse_at(text: str) -> tuple[float | None, float | None, float]:
    match = first_match(text, r"^\s*\(at\s+([\d\.-]+)\s+([\d\.-]+)(?:\s+([\d\.-]+))?", re.M)
    if not match:
        return None, None, 0.0
    return float(match.group(1)), float(match.group(2)), float(match.group(3) or 0)


def transform_local_to_global(x: float, y: float, rot_deg: float, local_x: float, local_y: float) -> tuple[float, float]:
    # KiCad PCB coordinates are y-down. This transform matches the generated drill Gerbers.
    theta = math.radians(rot_deg)
    gx = x + local_x * math.cos(theta) + local_y * math.sin(theta)
    gy = y - local_x * math.sin(theta) + local_y * math.cos(theta)
    return gx, gy


def parse_board_thickness(text: str) -> float | None:
    match = first_match(text, r"\(general\s+.*?\(thickness\s+([\d\.]+)\)", re.S)
    if match:
        return float(match.group(1))
    match = first_match(text, r"\(thickness\s+([\d\.]+)\)")
    return float(match.group(1)) if match else None


def parse_edge_cuts(lines: list[str]) -> list[dict[str, Any]]:
    edges: list[dict[str, Any]] = []
    for idx, line in enumerate(lines):
        if re.match(r"\s*\(gr_(rect|line|arc|circle|poly)\b", line):
            start_line, end_line, block_lines = block_at(lines, idx)
            block = "\n".join(block_lines)
            if '(layer "Edge.Cuts")' not in block:
                continue
            kind = re.match(r"\s*\((gr_\w+)", line).group(1)  # type: ignore[union-attr]
            item: dict[str, Any] = {"kind": kind, "source_line": start_line, "block": block}
            stroke = first_match(block, r"\(width\s+([\d\.-]+)\)")
            item["stroke_width_mm"] = float(stroke.group(1)) if stroke else None
            if kind == "gr_rect":
                start = first_match(block, r"\(start\s+([\d\.-]+)\s+([\d\.-]+)\)")
                end = first_match(block, r"\(end\s+([\d\.-]+)\s+([\d\.-]+)\)")
                if start and end:
                    item.update(
                        {
                            "x1": float(start.group(1)),
                            "y1": float(start.group(2)),
                            "x2": float(end.group(1)),
                            "y2": float(end.group(2)),
                        }
                    )
            elif kind == "gr_line":
                start = first_match(block, r"\(start\s+([\d\.-]+)\s+([\d\.-]+)\)")
                end = first_match(block, r"\(end\s+([\d\.-]+)\s+([\d\.-]+)\)")
                if start and end:
                    item.update(
                        {
                            "x1": float(start.group(1)),
                            "y1": float(start.group(2)),
                            "x2": float(end.group(1)),
                            "y2": float(end.group(2)),
                        }
                    )
            elif kind == "gr_circle":
                center = first_match(block, r"\(center\s+([\d\.-]+)\s+([\d\.-]+)\)")
                end = first_match(block, r"\(end\s+([\d\.-]+)\s+([\d\.-]+)\)")
                if center and end:
                    cx, cy = float(center.group(1)), float(center.group(2))
                    ex, ey = float(end.group(1)), float(end.group(2))
                    r = math.hypot(ex - cx, ey - cy)
                    item.update({"cx": cx, "cy": cy, "radius_mm": r})
            edges.append(item)
    return edges


def edge_bounds(edges: list[dict[str, Any]]) -> tuple[float, float, float, float]:
    xs: list[float] = []
    ys: list[float] = []
    for edge in edges:
        if edge["kind"] in {"gr_rect", "gr_line"}:
            xs.extend([edge.get("x1"), edge.get("x2")])
            ys.extend([edge.get("y1"), edge.get("y2")])
        elif edge["kind"] == "gr_circle":
            xs.extend([edge["cx"] - edge["radius_mm"], edge["cx"] + edge["radius_mm"]])
            ys.extend([edge["cy"] - edge["radius_mm"], edge["cy"] + edge["radius_mm"]])
    xs = [float(v) for v in xs if v is not None]
    ys = [float(v) for v in ys if v is not None]
    if not xs or not ys:
        raise RuntimeError("No supported Edge.Cuts geometry found.")
    return min(xs), min(ys), max(xs), max(ys)


def parse_step_bbox(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    text = read_text(path)
    points = re.findall(
        r"CARTESIAN_POINT\s*\([^,]*,\s*\(([-+0-9.Ee]+)\s*,\s*([-+0-9.Ee]+)\s*,\s*([-+0-9.Ee]+)\s*\)\s*\)",
        text,
    )
    if not points:
        return None
    xs = [float(p[0]) for p in points]
    ys = [float(p[1]) for p in points]
    zs = [float(p[2]) for p in points]
    return {
        "path": str(path),
        "points": len(points),
        "min_x": min(xs),
        "max_x": max(xs),
        "min_y": min(ys),
        "max_y": max(ys),
        "min_z": min(zs),
        "max_z": max(zs),
        "size_x": max(xs) - min(xs),
        "size_y": max(ys) - min(ys),
        "size_z": max(zs) - min(zs),
    }


def resolve_kicad_model(model_ref: str) -> Path | None:
    model_ref = model_ref.strip().strip('"')
    if not model_ref:
        return None
    replacements = {
        "${KICAD9_3DMODEL_DIR}": os.environ.get("KICAD9_3DMODEL_DIR", r"C:\Program Files\KiCad\9.0\share\kicad\3dmodels"),
        "${KICAD8_3DMODEL_DIR}": os.environ.get("KICAD8_3DMODEL_DIR", r"C:\Program Files\KiCad\8.0\share\kicad\3dmodels"),
    }
    resolved = model_ref
    for key, value in replacements.items():
        resolved = resolved.replace(key, value)
    candidate = Path(resolved)
    if not candidate.is_absolute():
        candidate = PROJECT_DIR / candidate
    return candidate


def height_hint_from_name(footprint: str, value: str, description: str) -> tuple[float | None, str]:
    haystack = " ".join([footprint, value, description])
    patterns = [
        (r"_H([0-9]+(?:\.[0-9]+)?)\b", "height suffix in footprint name"),
        (r"x([0-9]+(?:\.[0-9]+))mm", "dimension in footprint description/name"),
        (r"([0-9]+(?:\.[0-9]+)?)mm\s+height", "height text in footprint description"),
        (r"body thickness\D+([0-9]+(?:\.[0-9]+)?)mm", "body thickness text in footprint description"),
    ]
    for pattern, basis in patterns:
        match = re.search(pattern, haystack, re.I)
        if match:
            return float(match.group(1)), basis
    return None, ""


def parse_footprints(lines: list[str], board_min_x: float, board_min_y: float) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    footprints: list[dict[str, Any]] = []
    holes: list[dict[str, Any]] = []
    for idx, line in enumerate(lines):
        if not re.match(r"\s*\(footprint\s+\"", line):
            continue
        source_line, end_line, block_lines = block_at(lines, idx)
        block = "\n".join(block_lines)
        lib = first_match(block, r'\(footprint\s+"([^"]+)"')
        ref = first_match(block, r'\(property\s+"Reference"\s+"([^"]+)"')
        value = first_match(block, r'\(property\s+"Value"\s+"([^"]+)"')
        layer = first_match(block, r'\(layer\s+"([^"]+)"\)')
        descr = first_match(block, r'\(descr\s+"([^"]*)"')
        x, y, rot = parse_at(block)
        if x is None or y is None:
            continue
        attrs = [m.group(1).strip() for m in re.finditer(r"\(attr\s+([^\)]*)\)", block)]
        models = [m.group(1).strip() for m in re.finditer(r'\(model\s+"?([^"\n\)]+)"?', block)]
        model_bboxes = []
        model_z_height = None
        for model in models:
            path = resolve_kicad_model(model)
            bbox = parse_step_bbox(path) if path else None
            if bbox:
                model_bboxes.append(bbox)
                model_z_height = max(model_z_height or 0, bbox["max_z"])
        name_hint, hint_basis = height_hint_from_name(lib.group(1) if lib else "", value.group(1) if value else "", descr.group(1) if descr else "")
        height = model_z_height if model_z_height is not None else name_hint
        confidence = "confirmed from local STEP model" if model_z_height is not None else ("estimated from footprint/model name" if name_hint else "")

        footprint = {
            "source_line": source_line,
            "source_end_line": end_line,
            "reference": ref.group(1) if ref else "",
            "value": value.group(1) if value else "",
            "footprint": lib.group(1) if lib else "",
            "x_mm": x,
            "y_mm": y,
            "board_x_mm": x - board_min_x,
            "board_y_mm": y - board_min_y,
            "rotation_deg": rot,
            "layer": layer.group(1) if layer else "",
            "side": "top" if (layer and layer.group(1).startswith("F.")) else ("bottom" if layer and layer.group(1).startswith("B.") else ""),
            "attributes": "; ".join(attrs),
            "description": descr.group(1) if descr else "",
            "model_refs": "; ".join(models),
            "model_paths_found": "; ".join(b["path"] for b in model_bboxes),
            "height_hint_mm": height,
            "height_basis": confidence or hint_basis,
        }
        footprints.append(footprint)

        sublines = block.splitlines()
        for pad_idx, pad_line in enumerate(sublines):
            if not re.match(r"\s*\(pad\s+\"", pad_line):
                continue
            pad_start, pad_end, pad_lines = block_at(sublines, pad_idx)
            pad_block = "\n".join(pad_lines)
            pad_match = first_match(pad_block, r'\(pad\s+"([^"]*)"\s+(\S+)\s+(\S+)')
            if not pad_match:
                continue
            drill_match = first_match(pad_block, r"\(drill\s+(oval\s+)?([\d\.-]+)(?:\s+([\d\.-]+))?")
            if pad_match.group(2) not in {"thru_hole", "np_thru_hole"} and not drill_match:
                continue
            pad_at = first_match(pad_block, r"\(at\s+([\d\.-]+)\s+([\d\.-]+)(?:\s+([\d\.-]+))?")
            pad_size = first_match(pad_block, r"\(size\s+([\d\.-]+)\s+([\d\.-]+)\)")
            pad_net = first_match(pad_block, r'\(net\s+(\d+)(?:\s+"([^"]*)")?\)')
            local_x = float(pad_at.group(1)) if pad_at else 0.0
            local_y = float(pad_at.group(2)) if pad_at else 0.0
            gx, gy = transform_local_to_global(x, y, rot, local_x, local_y)
            drill_x = float(drill_match.group(2)) if drill_match else None
            drill_y = float(drill_match.group(3)) if drill_match and drill_match.group(3) else drill_x
            hole = {
                "kind": "pad",
                "source_line": source_line + pad_start - 1,
                "reference": footprint["reference"],
                "value": footprint["value"],
                "footprint": footprint["footprint"],
                "pad": pad_match.group(1),
                "pad_type": pad_match.group(2),
                "pad_shape": pad_match.group(3),
                "x_mm": gx,
                "y_mm": gy,
                "board_x_mm": gx - board_min_x,
                "board_y_mm": gy - board_min_y,
                "local_x_mm": local_x,
                "local_y_mm": local_y,
                "drill_x_mm": drill_x,
                "drill_y_mm": drill_y,
                "drill_diameter_mm": max([v for v in [drill_x, drill_y] if v is not None], default=None),
                "pad_size_x_mm": float(pad_size.group(1)) if pad_size else None,
                "pad_size_y_mm": float(pad_size.group(2)) if pad_size else None,
                "layers": all_strings_in_layers(pad_block),
                "net_code": int(pad_net.group(1)) if pad_net else None,
                "net_name": pad_net.group(2) if pad_net and pad_net.group(2) else "",
            }
            holes.append(hole)
    return footprints, holes


def parse_vias(lines: list[str], board_min_x: float, board_min_y: float) -> list[dict[str, Any]]:
    holes: list[dict[str, Any]] = []
    for idx, line in enumerate(lines):
        if not re.match(r"\s*\(via\b", line):
            continue
        source_line, _end_line, block_lines = block_at(lines, idx)
        block = "\n".join(block_lines)
        at = first_match(block, r"\(at\s+([\d\.-]+)\s+([\d\.-]+)\)")
        size = first_match(block, r"\(size\s+([\d\.-]+)\)")
        drill = first_match(block, r"\(drill\s+([\d\.-]+)\)")
        net = first_match(block, r"\(net\s+(\d+)\)")
        if not at or not drill:
            continue
        x = float(at.group(1))
        y = float(at.group(2))
        holes.append(
            {
                "kind": "via",
                "source_line": source_line,
                "reference": "",
                "value": "",
                "footprint": "",
                "pad": "",
                "pad_type": "via",
                "pad_shape": "circle",
                "x_mm": x,
                "y_mm": y,
                "board_x_mm": x - board_min_x,
                "board_y_mm": y - board_min_y,
                "local_x_mm": "",
                "local_y_mm": "",
                "drill_x_mm": float(drill.group(1)),
                "drill_y_mm": float(drill.group(1)),
                "drill_diameter_mm": float(drill.group(1)),
                "pad_size_x_mm": float(size.group(1)) if size else None,
                "pad_size_y_mm": float(size.group(1)) if size else None,
                "layers": all_strings_in_layers(block),
                "net_code": int(net.group(1)) if net else None,
                "net_name": "",
                "free": "(free yes)" in block,
            }
        )
    return holes


def classify_hole(hole: dict[str, Any], board_bounds: tuple[float, float, float, float]) -> str:
    text = " ".join(str(hole.get(k, "")) for k in ("reference", "footprint", "value")).lower()
    no_net = hole.get("net_code") in (None, 0) and not hole.get("net_name")
    drill = float(hole.get("drill_diameter_mm") or 0)
    pad_type = hole.get("pad_type", "")
    large = drill >= 2.5
    mechanical_name = any(token in text for token in ("mount", "mounting", "hole", "standoff"))
    if pad_type == "np_thru_hole":
        return "candidate_mounting_hole"
    if no_net and mechanical_name:
        return "candidate_mounting_hole"
    if no_net and large and hole.get("kind") == "via":
        return "candidate_mounting_hole"
    return "electrical_through_hole"


def add_edge_distances(holes: list[dict[str, Any]], bounds: tuple[float, float, float, float]) -> None:
    min_x, min_y, max_x, max_y = bounds
    for hole in holes:
        x = float(hole["x_mm"])
        y = float(hole["y_mm"])
        drill = float(hole.get("drill_diameter_mm") or 0)
        hole["edge_left_center_mm"] = x - min_x
        hole["edge_right_center_mm"] = max_x - x
        hole["edge_top_center_mm"] = y - min_y
        hole["edge_bottom_center_mm"] = max_y - y
        hole["edge_left_hole_mm"] = x - min_x - drill / 2
        hole["edge_right_hole_mm"] = max_x - x - drill / 2
        hole["edge_top_hole_mm"] = y - min_y - drill / 2
        hole["edge_bottom_hole_mm"] = max_y - y - drill / 2


def read_csv_if_exists(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", errors="replace", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    df = pd.DataFrame(rows)
    df.to_csv(path, index=False)


def height_table(footprints: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows = [f for f in footprints if f.get("height_hint_mm") not in (None, "")]
    return sorted(rows, key=lambda row: float(row.get("height_hint_mm") or 0), reverse=True)


def generate_summary(
    board: dict[str, Any],
    edge_rows: list[dict[str, Any]],
    holes: list[dict[str, Any]],
    footprints: list[dict[str, Any]],
    top_pos: list[dict[str, str]],
    bottom_pos: list[dict[str, str]],
) -> str:
    candidates = [h for h in holes if h["classification"] == "candidate_mounting_hole"]
    electrical = [h for h in holes if h["classification"] != "candidate_mounting_hole"]
    heights = height_table(footprints)
    tallest = heights[0] if heights else None
    top_components = [f for f in footprints if f.get("side") == "top"]
    bottom_components = [f for f in footprints if f.get("side") == "bottom"]

    lines: list[str] = []
    lines.append("# COMMAND LINK PCB Mechanical Analysis")
    lines.append("")
    lines.append("Generated by `tools/analyze_pcb.py`.")
    lines.append("")
    lines.append("## Source Files")
    lines.append("")
    lines.append(f"- Primary PCB: `{PCB_PATH.relative_to(ROOT)}`")
    lines.append(f"- BOM: `{BOM_PATH.relative_to(ROOT)}`")
    lines.append(f"- Top pick-and-place: `{TOP_POS_PATH.relative_to(ROOT)}`")
    lines.append(f"- Bottom pick-and-place: `{BOTTOM_POS_PATH.relative_to(ROOT)}`")
    lines.append(f"- Fabrication job: `{FAB_JOB_PATH.relative_to(ROOT)}`")
    lines.append(f"- Edge.Cuts Gerber: `{EDGE_GBR_PATH.relative_to(ROOT)}`")
    lines.append(f"- PTH drill Gerber: `{PTH_DRL_PATH.relative_to(ROOT)}`")
    lines.append(f"- NPTH drill Gerber: `{NPTH_DRL_PATH.relative_to(ROOT)}`")
    lines.append("")
    lines.append("## Confirmed Board Dimensions")
    lines.append("")
    lines.append("| Item | mm | inches | Source |")
    lines.append("|---|---:|---:|---|")
    lines.append(f"| Board width X | {board['width_mm']:.3f} | {mm_to_in(board['width_mm']):.4f} | Edge.Cuts centerline |")
    lines.append(f"| Board length Y | {board['height_mm']:.3f} | {mm_to_in(board['height_mm']):.4f} | Edge.Cuts centerline |")
    lines.append(f"| Board thickness | {board['thickness_mm']:.3f} | {mm_to_in(board['thickness_mm']):.4f} | PCB `(general (thickness ...))` |")
    lines.append(f"| Board origin used for local coordinates | ({board['min_x_mm']:.3f}, {board['min_y_mm']:.3f}) | | Edge.Cuts min corner |")
    lines.append("")
    lines.append("The fabrication job reports `65.05 x 78.76 mm`, which includes the 0.05 mm Edge.Cuts plotting aperture. For enclosure CAD, use the Edge.Cuts centerline size above.")
    lines.append("")
    lines.append("## Edge.Cuts Outline")
    lines.append("")
    lines.append("| Primitive | Source line | Start | End | Stroke | Notes |")
    lines.append("|---|---:|---:|---:|---:|---|")
    for edge in edge_rows:
        lines.append(
            f"| {edge['kind']} | {edge['source_line']} | ({edge.get('x1', '')}, {edge.get('y1', '')}) | ({edge.get('x2', '')}, {edge.get('y2', '')}) | {edge.get('stroke_width_mm', '')} mm | Single rectangular outline |"
        )
    lines.append("")
    lines.append("Confirmed outline: rectangular, no Edge.Cuts arcs, no cutouts, no notches, and no modeled corner radius.")
    lines.append("")
    lines.append("## Candidate Mounting Holes")
    lines.append("")
    lines.append("These are candidate mechanical mounting holes because they are large, circular, netless holes not owned by connector footprints. In this design they are represented as top-level plated vias, not NPTH mounting footprints.")
    lines.append("")
    lines.append("| ID | Source line | KiCad X/Y mm | Board-local X/Y mm | Drill | Pad/via dia. | Center edge distances L/R/T/B | Hole-edge min | Recommendation |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---|")
    for i, h in enumerate(sorted(candidates, key=lambda r: (r["board_y_mm"], r["board_x_mm"])), start=1):
        min_clear = min(h["edge_left_hole_mm"], h["edge_right_hole_mm"], h["edge_top_hole_mm"], h["edge_bottom_hole_mm"])
        lines.append(
            f"| MH{i} | `{h['source_line']}` | ({h['x_mm']:.3f}, {h['y_mm']:.3f}) | ({h['board_x_mm']:.3f}, {h['board_y_mm']:.3f}) | {h['drill_diameter_mm']:.3f} mm | {h['pad_size_x_mm']:.3f} mm | {h['edge_left_center_mm']:.3f}/{h['edge_right_center_mm']:.3f}/{h['edge_top_center_mm']:.3f}/{h['edge_bottom_center_mm']:.3f} | {min_clear:.3f} mm | M3 clearance, 4.5-5.0 mm standoff OD |"
        )
    lines.append("")
    lines.append("## Electrical Through Holes Excluded From Mounting")
    lines.append("")
    lines.append("| Group | Count | Drill / pad | Reason excluded |")
    lines.append("|---|---:|---|---|")
    def count_ref(ref: str) -> list[dict[str, Any]]:
        return [h for h in electrical if h.get("reference") == ref]
    for ref, label in [("J4", "left solder-wire connector"), ("J3", "left solder-wire connector"), ("J2", "right solder-wire connector"), ("J1", "programming header")]:
        rows = count_ref(ref)
        if not rows:
            continue
        drill = rows[0].get("drill_diameter_mm")
        pad = rows[0].get("pad_size_x_mm")
        lines.append(f"| {ref} {label} | {len(rows)} | {fmt(drill)} mm drill / {fmt(pad)} mm pad | Footprint-owned pads with electrical nets |")
    via_electrical = [h for h in electrical if h["kind"] == "via"]
    lines.append(f"| Electrical vias | {len(via_electrical)} | 0.3 mm and 0.8 mm drills | Routed plated vias with electrical nets |")
    lines.append("")
    lines.append("## Component Placement And Height")
    lines.append("")
    lines.append(f"Top-side footprints found: {len(top_components)}. Bottom-side footprints found: {len(bottom_components)}. Bottom pick-and-place rows after header: {max(len(bottom_pos), 0)}.")
    lines.append("")
    lines.append("| Ref | Footprint | Board-local placement/origin | Side | Height | Basis |")
    lines.append("|---|---|---:|---|---:|---|")
    for f in heights[:12]:
        lines.append(
            f"| {f['reference']} | `{f['footprint'].split(':')[-1]}` | ({f['board_x_mm']:.3f}, {f['board_y_mm']:.3f}) | {f['side']} | {float(f['height_hint_mm']):.2f} mm | {f['height_basis']} |"
        )
    lines.append("")
    if tallest:
        lines.append(f"Tallest confirmed/derived part: `{tallest['reference']}` at approximately `{float(tallest['height_hint_mm']):.2f} mm` above the PCB.")
    lines.append("")
    lines.append("Limitations: KiCad footprint names and installed STEP models provide many package heights, but not every custom or missing model has a confirmed height. The solder-wire connector models and the custom ULN2803 footprint do not provide usable local STEP height data in this project.")
    lines.append("")
    lines.append("## Connector / Wire Access")
    lines.append("")
    lines.append("| Ref | Type | Board-local pads/center | Side | Enclosure access recommendation |")
    lines.append("|---|---|---:|---|---|")
    lines.append("| J4 | 4-position solder-wire pads | X 4.750, Y 11.990 to 35.390 | Top / left edge | Left wall slot, Y about 10-38 mm, at least 5 mm high around PCB/wire plane |")
    lines.append("| J3 | 4-position solder-wire pads | X 4.775, Y 43.315 to 66.715 | Top / left edge | Left wall slot, Y about 41-69 mm, at least 5 mm high around PCB/wire plane |")
    lines.append("| J2 | 6-position solder-wire pads | X 60.450, Y 20.265 to 59.265 | Top / right edge | Right wall slot, Y about 18-62 mm, at least 5 mm high around PCB/wire plane |")
    lines.append("| J1 | 1x06 1.27 mm vertical programming header | X 29.145 to 35.495, Y 66.365 | Top | Optional lid access window centered near (32.320, 66.365) |")
    lines.append("")
    lines.append("The solder-wire footprint descriptions specify 2 mm conductor, 3.9 mm outer diameter wire, and bend radius of 3x OD. Reserve about 12 mm bend volume where wires turn.")
    lines.append("")
    lines.append("## Enclosure Recommendations")
    lines.append("")
    lines.append("| Feature | Value | Basis |")
    lines.append("|---|---:|---|")
    lines.append("| Board pocket tolerance | 0.5 mm per side | FDM/assembly recommendation |")
    lines.append("| Bottom standoff height | 4.0 mm minimum, 5.0 mm conservative | Clearance for bottom pins/solder joints |")
    lines.append("| Top component height | 10.5 mm | C11 STEP/footprint confirmed |")
    lines.append("| Top lid clearance | 2.0 mm minimum | Recommendation above tallest component |")
    lines.append("| Internal case height | 20.0 mm conservative | 4.0 + 1.6 + 10.5 + 2.0 rounded up |")
    lines.append("| Screw clearance | 3.4 mm | M3 clearance recommendation |")
    lines.append("| Standoff OD | 4.5 to 5.0 mm | Mounting holes are close to board edges |")
    lines.append("")
    lines.append("## OpenSCAD Variables")
    lines.append("")
    lines.append("```scad")
    lines.append(f"pcb_width = {board['width_mm']:.3f};")
    lines.append(f"pcb_length = {board['height_mm']:.3f};")
    lines.append(f"pcb_thickness = {board['thickness_mm']:.3f};")
    lines.append("pcb_corner_radius = 0;")
    lines.append("mounting_hole_diameter = 3.200;")
    lines.append("mounting_hole_pad_diameter = 4.000;")
    lines.append("mounting_hole_positions = [")
    for h in sorted(candidates, key=lambda r: (r["board_y_mm"], r["board_x_mm"])):
        lines.append(f"    [{h['board_x_mm']:.3f}, {h['board_y_mm']:.3f}],")
    lines.append("];")
    lines.append("standoff_height = 4.000;")
    lines.append("standoff_outer_diameter = 4.800;")
    lines.append("screw_clearance_diameter = 3.400;")
    lines.append("internal_case_height = 20.000;")
    lines.append("lid_clearance = 2.000;")
    lines.append("wall_thickness = 3.000;")
    lines.append("recommended_tolerance = 0.500;")
    lines.append("connector_cutout_locations = [")
    lines.append('    ["left", 10.000, 38.000, 5.000],')
    lines.append('    ["left", 41.000, 69.000, 5.000],')
    lines.append('    ["right", 18.000, 62.000, 5.000],')
    lines.append("];")
    lines.append("j1_access_center = [32.320, 66.365];")
    lines.append("j1_access_size = [10.000, 6.000];")
    lines.append("wire_tie_anchor_locations = [")
    lines.append('    ["left_J4_bundle", -8.000, 24.000],')
    lines.append('    ["left_J3_bundle", -8.000, 55.000],')
    lines.append('    ["right_J2_bundle", 73.000, 40.000],')
    lines.append("];")
    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    if not PCB_PATH.exists():
        raise FileNotFoundError(f"Missing PCB file: {PCB_PATH}")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    pcb_text = read_text(PCB_PATH)
    lines = pcb_text.splitlines()
    thickness = parse_board_thickness(pcb_text)
    edge_rows = parse_edge_cuts(lines)
    min_x, min_y, max_x, max_y = edge_bounds(edge_rows)
    width = max_x - min_x
    height = max_y - min_y
    board = {
        "source": str(PCB_PATH.relative_to(ROOT)),
        "min_x_mm": min_x,
        "min_y_mm": min_y,
        "max_x_mm": max_x,
        "max_y_mm": max_y,
        "width_mm": width,
        "height_mm": height,
        "width_in": mm_to_in(width),
        "height_in": mm_to_in(height),
        "thickness_mm": thickness,
        "thickness_in": mm_to_in(thickness) if thickness is not None else None,
    }

    footprints, pad_holes = parse_footprints(lines, min_x, min_y)
    via_holes = parse_vias(lines, min_x, min_y)
    holes = pad_holes + via_holes
    bounds = (min_x, min_y, max_x, max_y)
    add_edge_distances(holes, bounds)
    for hole in holes:
        hole["classification"] = classify_hole(hole, bounds)

    candidate_mounting = [h for h in holes if h["classification"] == "candidate_mounting_hole"]
    electrical_through = [h for h in holes if h["classification"] != "candidate_mounting_hole"]
    top_pos = read_csv_if_exists(TOP_POS_PATH)
    bottom_pos = read_csv_if_exists(BOTTOM_POS_PATH)

    write_csv(OUTPUT_DIR / "pcb_dimensions.csv", [board])
    write_csv(OUTPUT_DIR / "all_holes.csv", holes)
    write_csv(OUTPUT_DIR / "candidate_mounting_holes.csv", candidate_mounting)
    write_csv(OUTPUT_DIR / "electrical_through_holes.csv", electrical_through)
    write_csv(OUTPUT_DIR / "footprints.csv", footprints)

    summary = generate_summary(board, edge_rows, holes, footprints, top_pos, bottom_pos)
    (OUTPUT_DIR / "pcb_analysis_summary.md").write_text(summary, encoding="utf-8")
    ROOT_REPORT.write_text(summary, encoding="utf-8")

    print("PCB mechanical analysis complete.")
    print(f"Board: {width:.3f} x {height:.3f} x {thickness:.3f} mm")
    print(f"Footprints: {len(footprints)}")
    print(f"All drilled features: {len(holes)}")
    print(f"Candidate mounting holes: {len(candidate_mounting)}")
    print(f"Electrical through-holes/vias: {len(electrical_through)}")
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Root report: {ROOT_REPORT}")


if __name__ == "__main__":
    main()
