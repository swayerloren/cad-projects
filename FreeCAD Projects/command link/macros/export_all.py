"""Build and export all COMMAND LINK FreeCAD replication deliverables."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from command_link_freecad_common import FCSTD_PATH, export_all


if __name__ == "__main__":
    results = export_all()
    print("Created", FCSTD_PATH)
    for name, ok in results.items():
        print(f"{name}: {'PASS' if ok else 'FAIL'}")
