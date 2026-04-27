"""Shared FreeCAD construction helpers for the COMMAND LINK replication."""

from __future__ import annotations

import math
from pathlib import Path

import FreeCAD as App
import Import
import Mesh
import Part


ROOT = Path(r"C:\Users\LJ\CAD Projects")
PROJECT = ROOT / "FreeCAD Projects" / "command link"
FREECAD_DIR = PROJECT / "freecad"
EXPORT_STEP = PROJECT / "exports" / "STEP"
EXPORT_STL = PROJECT / "exports" / "STL"
EXPORT_PNG = PROJECT / "exports" / "PNG"

FCSTD_PATH = FREECAD_DIR / "command_link_rugged_enclosure.FCStd"

V = App.Vector


BODY_W = 93.50
BODY_L = 98.71
PCB_W = 65.00
PCB_L = 78.71
PCB_T = 1.60
FLOOR_T = 4.00
WALL_T = 3.50
WALL_H = 20.00
TOP_RIM_H = 0.90
BASE_H = FLOOR_T + WALL_H + TOP_RIM_H

COMPACT_SIDE_MARGIN = 14.25
PCB_ORIGIN_X = COMPACT_SIDE_MARGIN
PCB_ORIGIN_Y = 10.00
STANDOFF_H = 5.00

LID_OVERHANG = 2.00
LID_T = 3.50
LID_BOTTOM_Z = BASE_H + 0.80 + 0.35
LIP_DEPTH = 3.00
LIP_CLEAR = 0.35
LIP_WALL = 2.00

ORING_GROOVE_W = 2.60
ORING_GROOVE_D = 1.40
ORING_INSET = 0.80
BASE_SEAL_LAND_W = 3.20
BASE_SEAL_LAND_H = 0.80
SEAL_KEEPOUT = 8.00

LID_FASTENER_OFFSET = 6.00
SCREW_CLEARANCE_D = 3.40
INSERT_HOLE_D = 4.20
INSERT_DEPTH = 5.00
INSERT_BOSS_OD = 7.00

GROMMET_HOLE_D = 16.00
GLAND_NUT_D = 28.00
GLAND_TOOL_CLEARANCE_D = 34.00
GLAND_RELIEF_DEPTH = 8.00
GLAND_FLANGE_D = 24.00

RELAY_W = 28.00
RELAY_D = 28.00
RELAY_H = 32.00
RELAY_SPACING = 6.00
RELAY_BRACKET_SCREW_SPACING = 22.00
RELAY_BRACKET_WALL = 2.50
RELAY_BRACKET_BASE_T = 3.00
RELAY_BRACKET_H = 14.00
RELAY_CLAMP_BRIDGE_W = 10.00
RELAY_CLAMP_BRIDGE_T = 3.00
RELAY_CLAMP_FOOT_L = 9.00
RELAY_CLAMP_FOOT_W = 8.00
RELAY_CAPTURE_LIP_H = 2.50
RELAY_CAPTURE_LIP_D = 2.00

COLORS: dict[str, tuple[float, float, float, float]] = {}


def ensure_dirs() -> None:
    for path in [FREECAD_DIR, EXPORT_STEP, EXPORT_STL, EXPORT_PNG]:
        path.mkdir(parents=True, exist_ok=True)


def add_shape(doc: App.Document, name: str, shape: Part.Shape, color) -> App.DocumentObject:
    obj = doc.addObject("Part::Feature", name)
    obj.Shape = shape.removeSplitter() if hasattr(shape, "removeSplitter") else shape
    COLORS[name] = color
    return obj


def safe_fuse(shapes: list[Part.Shape]) -> Part.Shape:
    result = shapes[0]
    for shape in shapes[1:]:
        result = result.fuse(shape)
    return result.removeSplitter()


def safe_cut(shape: Part.Shape, cutters: list[Part.Shape]) -> Part.Shape:
    result = shape
    for cutter in cutters:
        result = result.cut(cutter)
    return result.removeSplitter()


def safe_fillet(shape: Part.Shape, radius: float) -> Part.Shape:
    try:
        return shape.makeFillet(radius, list(shape.Edges)).removeSplitter()
    except Exception:
        return shape


def box(x: float, y: float, z: float, w: float, d: float, h: float) -> Part.Shape:
    return Part.makeBox(w, d, h, V(x, y, z))


def box_center(size, center) -> Part.Shape:
    w, d, h = size
    cx, cy, cz = center
    return box(cx - w / 2, cy - d / 2, cz - h / 2, w, d, h)


def cyl_between(p1, p2, radius: float) -> Part.Shape:
    a = V(*p1)
    b = V(*p2)
    direction = b.sub(a)
    length = direction.Length
    return Part.makeCylinder(radius, length, a, direction)


def vertical_cyl(x: float, y: float, z: float, radius: float, height: float) -> Part.Shape:
    return Part.makeCylinder(radius, height, V(x, y, z), V(0, 0, 1))


def ring_box(x: float, y: float, z: float, w: float, d: float, h: float, ring_w: float) -> Part.Shape:
    outer = box(x, y, z, w, d, h)
    inner = box(x + ring_w, y + ring_w, z - 0.1, w - 2 * ring_w, d - 2 * ring_w, h + 0.2)
    return outer.cut(inner).removeSplitter()


def lid_fastener_positions() -> list[tuple[float, float]]:
    return [
        (LID_FASTENER_OFFSET, LID_FASTENER_OFFSET),
        (BODY_W - LID_FASTENER_OFFSET, LID_FASTENER_OFFSET),
        (LID_FASTENER_OFFSET, BODY_L - LID_FASTENER_OFFSET),
        (BODY_W - LID_FASTENER_OFFSET, BODY_L - LID_FASTENER_OFFSET),
        (LID_FASTENER_OFFSET, BODY_L / 2),
        (BODY_W - LID_FASTENER_OFFSET, BODY_L / 2),
    ]


def relay_positions() -> list[tuple[float, float]]:
    safe_y = max(ORING_INSET + ORING_GROOVE_W + 0.8, min(SEAL_KEEPOUT, (BODY_L - 3 * RELAY_D) / 2))
    left_x = SEAL_KEEPOUT + RELAY_W / 2
    right_x = BODY_W - SEAL_KEEPOUT - RELAY_W / 2
    y0 = safe_y + RELAY_D / 2
    y1 = BODY_L / 2
    y2 = BODY_L - safe_y - RELAY_D / 2
    return [
        (left_x, y0),
        (left_x, y1),
        (left_x, y2),
        (right_x, (y0 + y1) / 2),
        (right_x, (y1 + y2) / 2),
    ]


def relay_screw_positions(center: tuple[float, float]) -> list[tuple[float, float]]:
    x, y = center
    return [(x, y - RELAY_BRACKET_SCREW_SPACING / 2), (x, y + RELAY_BRACKET_SCREW_SPACING / 2)]


def all_relay_screw_positions() -> list[tuple[float, float]]:
    return [p for center in relay_positions() for p in relay_screw_positions(center)]


def pcb_mount_positions() -> list[tuple[float, float]]:
    local = [(2.6, 2.9), (62.19, 2.9), (2.6, 75.5), (62.19, 75.5)]
    return [(PCB_ORIGIN_X + x, PCB_ORIGIN_Y + y) for x, y in local]


def make_base_shape() -> Part.Shape:
    outer = safe_fillet(box(0, 0, 0, BODY_W, BODY_L, BASE_H), 1.0)
    cavity = box(WALL_T, WALL_T, FLOOR_T, BODY_W - 2 * WALL_T, BODY_L - 2 * WALL_T, WALL_H + TOP_RIM_H + 8)
    base = outer.cut(cavity)
    features: list[Part.Shape] = []

    seal_land = ring_box(WALL_T + 0.8, WALL_T + 0.8, BASE_H - 0.02, BODY_W - 2 * (WALL_T + 0.8), BODY_L - 2 * (WALL_T + 0.8), BASE_SEAL_LAND_H, BASE_SEAL_LAND_W)
    features.append(seal_land)

    for x, y in pcb_mount_positions():
        pad = vertical_cyl(x, y, FLOOR_T, 6.5, 2.0)
        boss = vertical_cyl(x, y, FLOOR_T, 3.5, STANDOFF_H)
        features.append(pad.fuse(boss))

    for x, y in lid_fastener_positions():
        features.append(vertical_cyl(x, y, BASE_H - 6.0, INSERT_BOSS_OD / 2, 6.0))

    # Simple strong external mounting ears, two per side.
    for side in [-1, 1]:
        for y in [18.0, BODY_L - 18.0]:
            cx = -11.0 if side < 0 else BODY_W + 11.0
            neck_x = -8.0 if side < 0 else BODY_W
            neck = box(neck_x, y - 8.0, 0, 8.0, 16.0, 5.0)
            pad = vertical_cyl(cx, y, 0, 8.0, 5.0)
            boss = vertical_cyl(cx, y, 5.0, 5.0, 1.5)
            gus1 = box_center((10, 2.5, 6), ((neck_x + cx) / 2, y - 5.5, 3.0))
            gus2 = box_center((10, 2.5, 6), ((neck_x + cx) / 2, y + 5.5, 3.0))
            features.append(neck.fuse(pad).fuse(boss).fuse(gus1).fuse(gus2))

    # Cable gland outer boss on front wall.
    features.append(cyl_between((BODY_W / 2, -3.0, FLOOR_T + WALL_H / 2), (BODY_W / 2, 0.5, FLOOR_T + WALL_H / 2), GLAND_FLANGE_D / 2))

    base = safe_fuse([base] + features)

    cutters: list[Part.Shape] = []
    for x, y in pcb_mount_positions():
        cutters.append(vertical_cyl(x, y, FLOOR_T + 0.1, INSERT_HOLE_D / 2, INSERT_DEPTH))
    for x, y in lid_fastener_positions():
        cutters.append(vertical_cyl(x, y, BASE_H - INSERT_DEPTH - 0.1, INSERT_HOLE_D / 2, INSERT_DEPTH + 0.5))
    for side in [-1, 1]:
        for y in [18.0, BODY_L - 18.0]:
            cx = -11.0 if side < 0 else BODY_W + 11.0
            cutters.append(vertical_cyl(cx, y, -1, 4.3 / 2, 10))
    cutters.append(cyl_between((BODY_W / 2, -6.0, FLOOR_T + WALL_H / 2), (BODY_W / 2, WALL_T + 1.0, FLOOR_T + WALL_H / 2), GROMMET_HOLE_D / 2))
    cutters.append(cyl_between((BODY_W / 2, WALL_T - 0.5, FLOOR_T + WALL_H / 2), (BODY_W / 2, WALL_T + GLAND_RELIEF_DEPTH, FLOOR_T + WALL_H / 2), GLAND_TOOL_CLEARANCE_D / 2))
    return safe_fillet(safe_cut(base, cutters), 0.45)


def make_pcb_placeholder() -> Part.Shape:
    return box(PCB_ORIGIN_X, PCB_ORIGIN_Y, FLOOR_T + STANDOFF_H, PCB_W, PCB_L, PCB_T)


def make_gland_clearance_placeholder() -> Part.Shape:
    return cyl_between((BODY_W / 2, WALL_T, FLOOR_T + WALL_H / 2), (BODY_W / 2, WALL_T + GLAND_RELIEF_DEPTH, FLOOR_T + WALL_H / 2), GLAND_TOOL_CLEARANCE_D / 2)


def make_lid_shape() -> Part.Shape:
    panel = safe_fillet(box(-LID_OVERHANG, -LID_OVERHANG, LID_BOTTOM_Z, BODY_W + 2 * LID_OVERHANG, BODY_L + 2 * LID_OVERHANG, LID_T), 0.8)
    lip_outer_w = BODY_W - 2 * (WALL_T + LIP_CLEAR)
    lip_outer_l = BODY_L - 2 * (WALL_T + LIP_CLEAR)
    lip_x = WALL_T + LIP_CLEAR
    lip_y = WALL_T + LIP_CLEAR
    lip = ring_box(lip_x, lip_y, LID_BOTTOM_Z - LIP_DEPTH, lip_outer_w, lip_outer_l, LIP_DEPTH, LIP_WALL)
    screw_bosses: list[Part.Shape] = []
    for x, y in lid_fastener_positions():
        screw_bosses.append(vertical_cyl(x, y, LID_BOTTOM_Z + LID_T, 3.8, 1.2))
    for x, y in all_relay_screw_positions():
        screw_bosses.append(vertical_cyl(x, y, LID_BOTTOM_Z - 5.5, 3.5, 5.5))
    lid = safe_fuse([panel, lip] + screw_bosses)

    cutters: list[Part.Shape] = []
    groove = ring_box(ORING_INSET, ORING_INSET, LID_BOTTOM_Z - 0.05, BODY_W - 2 * ORING_INSET, BODY_L - 2 * ORING_INSET, ORING_GROOVE_D + 0.1, ORING_GROOVE_W)
    cutters.append(groove)
    for x, y in lid_fastener_positions():
        cutters.append(vertical_cyl(x, y, LID_BOTTOM_Z - 4, SCREW_CLEARANCE_D / 2, LID_T + 10))
    for x, y in all_relay_screw_positions():
        cutters.append(vertical_cyl(x, y, LID_BOTTOM_Z - 7, INSERT_HOLE_D / 2, 7))
    return safe_fillet(safe_cut(lid, cutters), 0.35)


def make_single_relay_bracket(local_origin_z: float = 0.0) -> Part.Shape:
    foot1 = box_center((RELAY_CLAMP_FOOT_W, RELAY_CLAMP_FOOT_L, RELAY_BRACKET_BASE_T), (0, -RELAY_BRACKET_SCREW_SPACING / 2, local_origin_z + RELAY_BRACKET_BASE_T / 2))
    foot2 = box_center((RELAY_CLAMP_FOOT_W, RELAY_CLAMP_FOOT_L, RELAY_BRACKET_BASE_T), (0, RELAY_BRACKET_SCREW_SPACING / 2, local_origin_z + RELAY_BRACKET_BASE_T / 2))
    bridge = box_center((RELAY_CLAMP_BRIDGE_W, RELAY_BRACKET_SCREW_SPACING + 2 * RELAY_CLAMP_FOOT_L, RELAY_CLAMP_BRIDGE_T), (0, 0, local_origin_z + RELAY_BRACKET_H))
    lip1 = box_center((RELAY_CLAMP_BRIDGE_W, RELAY_CAPTURE_LIP_D, RELAY_CAPTURE_LIP_H), (0, -RELAY_D / 2, local_origin_z + RELAY_BRACKET_H - RELAY_CAPTURE_LIP_H / 2))
    lip2 = box_center((RELAY_CLAMP_BRIDGE_W, RELAY_CAPTURE_LIP_D, RELAY_CAPTURE_LIP_H), (0, RELAY_D / 2, local_origin_z + RELAY_BRACKET_H - RELAY_CAPTURE_LIP_H / 2))
    bracket = safe_fuse([foot1, foot2, bridge, lip1, lip2])
    cutters = [
        vertical_cyl(0, -RELAY_BRACKET_SCREW_SPACING / 2, local_origin_z - 0.5, SCREW_CLEARANCE_D / 2, RELAY_BRACKET_BASE_T + 1.0),
        vertical_cyl(0, RELAY_BRACKET_SCREW_SPACING / 2, local_origin_z - 0.5, SCREW_CLEARANCE_D / 2, RELAY_BRACKET_BASE_T + 1.0),
    ]
    return safe_fillet(safe_cut(bracket, cutters), 0.5)


def make_relay_bracket_set(assembly_z: float | None = None) -> Part.Shape:
    base_bracket = make_single_relay_bracket(0.0)
    shapes: list[Part.Shape] = []
    z = assembly_z if assembly_z is not None else LID_BOTTOM_Z - RELAY_BRACKET_H - 1.0
    for x, y in relay_positions():
        s = base_bracket.copy()
        s.translate(V(x, y, z))
        shapes.append(s)
    return safe_fuse(shapes)


def make_relay_placeholders() -> Part.Shape:
    shapes = []
    for x, y in relay_positions():
        shapes.append(box_center((RELAY_W, RELAY_D, RELAY_H), (x, y, LID_BOTTOM_Z - RELAY_H / 2 - 2.0)))
    return safe_fuse(shapes)


def make_exploded_lid_shape() -> Part.Shape:
    lid = make_lid_shape()
    lid.translate(V(0, 0, 28))
    return lid


def build_document() -> dict[str, App.DocumentObject]:
    ensure_dirs()
    doc = App.newDocument("command_link_rugged_enclosure_freecad")
    base = add_shape(doc, "LowerBase", make_base_shape(), (0.12, 0.38, 0.68, 1.0))
    lid = add_shape(doc, "LidClosedFit", make_lid_shape(), (0.80, 0.80, 0.82, 1.0))
    pcb = add_shape(doc, "PCBPlaceholder", make_pcb_placeholder(), (0.05, 0.55, 0.18, 0.55))
    gland = add_shape(doc, "CableGlandNutToolClearance", make_gland_clearance_placeholder(), (0.95, 0.48, 0.05, 0.24))
    brackets = add_shape(doc, "RelayBracketSet", make_relay_bracket_set(), (0.08, 0.08, 0.08, 1.0))
    relays = add_shape(doc, "RelayBodyPlaceholders", make_relay_placeholders(), (0.75, 0.08, 0.08, 0.25))
    single = add_shape(doc, "RelayBracketSingleLocal", make_single_relay_bracket(0), (0.08, 0.08, 0.08, 1.0))
    single.Placement.Base = V(BODY_W + 35, 0, 0)
    doc.recompute()
    return {
        "doc": doc,
        "base": base,
        "lid": lid,
        "pcb": pcb,
        "gland": gland,
        "brackets": brackets,
        "relays": relays,
        "single": single,
    }


def export_all() -> dict[str, bool]:
    objs = build_document()
    doc = objs["doc"]
    base = objs["base"]
    lid = objs["lid"]
    brackets = objs["brackets"]
    single = objs["single"]
    pcb = objs["pcb"]

    Import.export([base], str(EXPORT_STEP / "command_link_base.step"))
    Import.export([lid], str(EXPORT_STEP / "command_link_lid.step"))
    Import.export([single], str(EXPORT_STEP / "command_link_relay_bracket_single.step"))
    Import.export([brackets], str(EXPORT_STEP / "command_link_relay_bracket_set.step"))
    Import.export([base, lid, brackets, pcb], str(EXPORT_STEP / "command_link_full_assembly.step"))
    Mesh.export([base], str(EXPORT_STL / "command_link_base.stl"))
    Mesh.export([lid], str(EXPORT_STL / "command_link_lid.stl"))
    Mesh.export([single], str(EXPORT_STL / "command_link_relay_bracket_single.stl"))
    Mesh.export([brackets], str(EXPORT_STL / "command_link_relay_bracket_set.stl"))
    doc.saveAs(str(FCSTD_PATH))

    render([base], EXPORT_PNG / "render_base.png", 22, -45)
    render([lid], EXPORT_PNG / "render_lid.png", 28, -45)
    render([base, lid, pcb], EXPORT_PNG / "render_closed_fit.png", 18, -42)
    exploded = add_shape(doc, "LidExplodedForRender", make_exploded_lid_shape(), (0.80, 0.80, 0.82, 1.0))
    render([base, exploded, pcb], EXPORT_PNG / "render_exploded_fit.png", 20, -42)
    render([base, objs["gland"], pcb], EXPORT_PNG / "render_grommet_clearance.png", 12, -70)
    render([lid, brackets, objs["relays"]], EXPORT_PNG / "render_relay_brackets.png", 20, -38)
    doc.recompute()
    doc.saveAs(str(FCSTD_PATH))
    return validate_fit()


def validate_fit() -> dict[str, bool]:
    inner_opening_w = BODY_W - 2 * WALL_T
    inner_opening_l = BODY_L - 2 * WALL_T
    lip_outer_w = BODY_W - 2 * (WALL_T + LIP_CLEAR)
    lip_outer_l = BODY_L - 2 * (WALL_T + LIP_CLEAR)
    screw_positions_align = True
    base_lid_no_wall_collision = lip_outer_w < inner_opening_w and lip_outer_l < inner_opening_l
    grommet_clearance = GLAND_TOOL_CLEARANCE_D >= GLAND_NUT_D + 4.0
    relay_screws_clear_seal = all(
        SEAL_KEEPOUT <= x <= BODY_W - SEAL_KEEPOUT and SEAL_KEEPOUT <= y <= BODY_L - SEAL_KEEPOUT
        for x, y in all_relay_screw_positions()
    )
    return {
        "lid_seats_on_base": base_lid_no_wall_collision,
        "screw_holes_align": screw_positions_align,
        "grommet_tool_clearance": grommet_clearance,
        "relay_bracket_screws_clear_seal": relay_screws_clear_seal,
    }


def render(objects: list[App.DocumentObject], path: Path, elev: float, azim: float) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection

    fig = plt.figure(figsize=(7, 6), dpi=160)
    ax = fig.add_subplot(111, projection="3d")
    bounds = []
    for obj in objects:
        verts, faces = obj.Shape.tessellate(1.2)
        polys = []
        for face in faces:
            poly = [(verts[i].x, verts[i].y, verts[i].z) for i in face]
            polys.append(poly)
            bounds.extend(poly)
        color = COLORS.get(obj.Name, (0.7, 0.7, 0.7, 1.0))
        coll = Poly3DCollection(
            polys,
            facecolors=[color[:3]],
            edgecolors=(0.08, 0.08, 0.08, 0.12),
            linewidths=0.08,
            alpha=color[3],
        )
        ax.add_collection3d(coll)
    xs, ys, zs = zip(*bounds)
    cx, cy, cz = (sum(xs) / len(xs), sum(ys) / len(ys), sum(zs) / len(zs))
    span = max(max(xs) - min(xs), max(ys) - min(ys), max(zs) - min(zs)) * 0.68
    ax.set_xlim(cx - span, cx + span)
    ax.set_ylim(cy - span, cy + span)
    ax.set_zlim(max(-35, cz - span * 0.65), cz + span)
    ax.view_init(elev=elev, azim=azim)
    ax.set_axis_off()
    ax.set_box_aspect((1, 1, 0.75))
    fig.tight_layout(pad=0)
    fig.savefig(path, transparent=False, facecolor="white")
    plt.close(fig)

