"""STL export macro template."""

from pathlib import Path

import FreeCAD as App
import Mesh


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "exports" / "STL" / "model.stl"


def export_stl():
    doc = App.ActiveDocument
    if doc is None:
        raise RuntimeError("Open or build a FreeCAD document before STL export.")
    objects = [obj for obj in doc.Objects if getattr(obj, "Shape", None)]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    Mesh.export(objects, str(OUT))


if __name__ == "__main__":
    export_stl()

