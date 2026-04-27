"""Build the Racing Seat Phone Stand FreeCAD replication.

This macro creates a FreeCAD document with imported STL references plus a
solid rebuild of the seat shell, rail/truss base, roll cage tube frame, screw
bosses, and phone fit-check placeholder. It exports STEP, STL, and PNG review
renders.
"""

from __future__ import annotations

import math
from pathlib import Path

import FreeCAD as App
import Import
import Mesh
import Part


ROOT = Path(r"C:\Users\LJ\CAD Projects")
PROJECT = ROOT / "FreeCAD Projects" / "racing seat phone stand"
SOURCE = ROOT / "pre made traiing models 3d" / "racing seat phone stand"
FREECAD_DIR = PROJECT / "freecad"
EXPORT_STEP = PROJECT / "exports" / "STEP"
EXPORT_STL = PROJECT / "exports" / "STL"
EXPORT_PNG = PROJECT / "exports" / "PNG"

FCSTD_PATH = FREECAD_DIR / "racing_seat_phone_stand.FCStd"
STEP_PATH = EXPORT_STEP / "racing_seat_phone_stand_freecad.step"
STL_PATH = EXPORT_STL / "racing_seat_phone_stand_freecad.stl"

V = App.Vector


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


def box_center(name: str, size, center) -> Part.Shape:
    w, d, h = size
    cx, cy, cz = center
    return Part.makeBox(w, d, h, V(cx - w / 2, cy - d / 2, cz - h / 2))


def cylinder_between(p1, p2, radius: float) -> Part.Shape:
    a = V(*p1)
    b = V(*p2)
    direction = b.sub(a)
    length = direction.Length
    if length <= 0:
        raise ValueError("Zero-length tube requested")
    return Part.makeCylinder(radius, length, a, direction)


def wire_section(y: float, width: float, z_floor: float, crown: float, bolster: float) -> Part.Wire:
    pts = [
        V(-width / 2, y, z_floor + bolster),
        V(-width * 0.36, y, z_floor),
        V(width * 0.36, y, z_floor),
        V(width / 2, y, z_floor + bolster),
        V(width * 0.46, y, z_floor + crown),
        V(-width * 0.46, y, z_floor + crown),
        V(-width / 2, y, z_floor + bolster),
    ]
    return Part.makePolygon(pts)


def make_seat_shell() -> Part.Shape:
    sections = [
        wire_section(-37, 62, 16, 15, 9),
        wire_section(-10, 65, 22, 20, 14),
        wire_section(18, 61, 45, 28, 18),
        wire_section(34, 52, 86, 26, 15),
    ]
    shell = Part.makeLoft(sections, True, False, False)
    cutters = [
        box_center("HarnessLeft", (9, 20, 22), (-14, 29, 82)),
        box_center("HarnessRight", (9, 20, 22), (14, 29, 82)),
        box_center("LowerHarness", (24, 18, 11), (0, 21, 55)),
        box_center("CableCutout", (20, 16, 12), (0, -38, 21)),
    ]
    shell = safe_cut(shell, cutters)
    return safe_fillet(shell, 1.2)


def make_cushion_insert() -> Part.Shape:
    cushion = box_center("Cushion", (42, 45, 3), (0, -8, 25))
    cushion.rotate(V(0, -6, 25), V(1, 0, 0), -12)
    back = box_center("BackCushion", (36, 4, 48), (0, 21, 65))
    back.rotate(V(0, 20, 45), V(1, 0, 0), -18)
    return safe_fillet(safe_fuse([cushion, back]), 1.0)


def make_rails_and_truss() -> tuple[Part.Shape, Part.Shape, Part.Shape]:
    rail_shapes: list[Part.Shape] = []
    truss_shapes: list[Part.Shape] = []
    boss_shapes: list[Part.Shape] = []
    for x in [-34, 34]:
        rail_shapes.append(safe_fillet(box_center("Rail", (8, 135, 4), (x, 0, 3)), 1.0))
        for y in [-52, 0, 52]:
            boss = Part.makeCylinder(5.2, 4.5, V(x, y, 4.0), V(0, 0, 1))
            hole = Part.makeCylinder(1.9, 7, V(x, y, 2.5), V(0, 0, 1))
            boss_shapes.append(boss.cut(hole))
    for side in [-1, 1]:
        x = side * 34
        truss_shapes.extend(
            [
                cylinder_between((x, -60, 5), (side * 13, -24, 18), 1.45),
                cylinder_between((side * 13, -24, 18), (x, 8, 5), 1.45),
                cylinder_between((x, 8, 5), (side * 12, 38, 18), 1.45),
                cylinder_between((side * 12, 38, 18), (x, 60, 5), 1.45),
                cylinder_between((x, -60, 5), (x, 60, 5), 1.25),
            ]
        )
    return safe_fuse(rail_shapes), safe_fuse(truss_shapes), safe_fuse(boss_shapes)


def make_roll_cage() -> Part.Shape:
    r = 1.75
    pts = {
        "lf": (-31, -37, 8),
        "rf": (31, -37, 8),
        "lr": (-31, 31, 8),
        "rr": (31, 31, 8),
        "lt": (-31, 30, 111),
        "rt": (31, 30, 111),
        "lm": (-32, -4, 74),
        "rm": (32, -4, 74),
    }
    tubes = [
        cylinder_between(pts["lr"], pts["lt"], r),
        cylinder_between(pts["rr"], pts["rt"], r),
        cylinder_between(pts["lt"], pts["rt"], r),
        cylinder_between(pts["lf"], pts["lm"], r),
        cylinder_between(pts["rf"], pts["rm"], r),
        cylinder_between(pts["lm"], pts["lt"], r),
        cylinder_between(pts["rm"], pts["rt"], r),
        cylinder_between(pts["lf"], pts["lr"], r),
        cylinder_between(pts["rf"], pts["rr"], r),
        cylinder_between(pts["lf"], pts["lt"], 1.35),
        cylinder_between(pts["rf"], pts["rt"], 1.35),
        cylinder_between(pts["lr"], pts["rm"], 1.25),
        cylinder_between(pts["rr"], pts["lm"], 1.25),
    ]
    return safe_fuse(tubes)


def make_phone_placeholder() -> Part.Shape:
    phone = box_center("Phone", (78, 8, 160), (0, -20, 78))
    phone.rotate(V(0, -34, 17), V(1, 0, 0), -15)
    return phone


def import_reference_meshes(doc: App.Document) -> None:
    refs = [
        SOURCE / "obj_1_Rollcage.stl",
        SOURCE / "obj_2_Seat.stl",
        SOURCE / "obj_3_Base SIlla racing Recaro v2.stl",
    ]
    for path in refs:
        if not path.exists():
            continue
        mesh_obj = doc.addObject("Mesh::Feature", "Reference_" + path.stem.replace(" ", "_"))
        mesh_obj.Mesh = Mesh.Mesh(str(path))


def build_document() -> tuple[App.Document, list[App.DocumentObject], App.DocumentObject]:
    ensure_dirs()
    doc = App.newDocument("racing_seat_phone_stand_freecad")
    import_reference_meshes(doc)

    seat = add_shape(doc, "SeatShellSolid", make_seat_shell(), (0.82, 0.05, 0.03, 1.0))
    cushion = add_shape(doc, "DarkCushionInsert", make_cushion_insert(), (0.02, 0.02, 0.025, 1.0))
    rails, truss, bosses = make_rails_and_truss()
    rail_obj = add_shape(doc, "SideRails", rails, (0.62, 0.62, 0.62, 1.0))
    truss_obj = add_shape(doc, "TriangularTrussWebbing", truss, (0.02, 0.02, 0.025, 1.0))
    boss_obj = add_shape(doc, "ScrewBossPads", bosses, (0.75, 0.75, 0.75, 1.0))
    cage_obj = add_shape(doc, "RollCageTubeFrame", make_roll_cage(), (0.01, 0.01, 0.012, 1.0))
    phone = add_shape(doc, "PhoneFitCheckPlaceholder", make_phone_placeholder(), (0.1, 0.35, 0.95, 0.30))
    doc.recompute()
    product = [seat, cushion, rail_obj, truss_obj, boss_obj, cage_obj]
    return doc, product, phone


def export_models(doc: App.Document, product: list[App.DocumentObject]) -> None:
    Import.export(product, str(STEP_PATH))
    Mesh.export(product, str(STL_PATH))
    doc.saveAs(str(FCSTD_PATH))


def render(objects: list[App.DocumentObject], path: Path, elev: float, azim: float) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection

    fig = plt.figure(figsize=(7, 6), dpi=160)
    ax = fig.add_subplot(111, projection="3d")
    bounds = []
    for obj in objects:
        if not hasattr(obj, "Shape"):
            continue
        verts, faces = obj.Shape.tessellate(1.0)
        if not verts or not faces:
            continue
        polys = []
        for face in faces:
            poly = [(verts[i].x, verts[i].y, verts[i].z) for i in face]
            polys.append(poly)
            bounds.extend(poly)
        color = COLORS.get(obj.Name, (0.7, 0.7, 0.7, 1.0))
        coll = Poly3DCollection(
            polys,
            facecolors=[color[:3]],
            edgecolors=(0.08, 0.08, 0.08, 0.15),
            linewidths=0.08,
            alpha=color[3],
        )
        ax.add_collection3d(coll)
    xs, ys, zs = zip(*bounds)
    cx, cy, cz = (sum(xs) / len(xs), sum(ys) / len(ys), sum(zs) / len(zs))
    span = max(max(xs) - min(xs), max(ys) - min(ys), max(zs) - min(zs)) * 0.62
    ax.set_xlim(cx - span, cx + span)
    ax.set_ylim(cy - span, cy + span)
    ax.set_zlim(max(0, cz - span * 0.55), cz + span * 1.05)
    ax.view_init(elev=elev, azim=azim)
    ax.set_axis_off()
    ax.set_box_aspect((1, 1, 1))
    fig.tight_layout(pad=0)
    fig.savefig(path, transparent=False, facecolor="white")
    plt.close(fig)


def main() -> None:
    doc, product, phone = build_document()
    export_models(doc, product)
    render(product, EXPORT_PNG / "render_front.png", 8, -90)
    render(product, EXPORT_PNG / "render_side.png", 10, 0)
    render(product, EXPORT_PNG / "render_iso.png", 24, -42)
    render(product + [phone], EXPORT_PNG / "phone_fit_check.png", 15, -38)
    print("Created", FCSTD_PATH)
    print("Exported", STEP_PATH)
    print("Exported", STL_PATH)


if __name__ == "__main__":
    main()

