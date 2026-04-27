"""STEP export macro template."""

from pathlib import Path

import FreeCAD as App
import Import


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "exports" / "STEP" / "model.step"


def export_step():
    doc = App.ActiveDocument
    if doc is None:
        raise RuntimeError("Open or build a FreeCAD document before STEP export.")
    objects = [obj for obj in doc.Objects if getattr(obj, "Shape", None)]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    Import.export(objects, str(OUT))


if __name__ == "__main__":
    export_step()

