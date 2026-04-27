"""Run COMMAND LINK FreeCAD base/lid fit checks."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from command_link_freecad_common import validate_fit


if __name__ == "__main__":
    for name, ok in validate_fit().items():
        print(f"{name}: {'PASS' if ok else 'FAIL'}")
