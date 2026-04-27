"""Build COMMAND LINK lower base FreeCAD geometry."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from command_link_freecad_common import build_document, FCSTD_PATH


if __name__ == "__main__":
    objs = build_document()
    objs["doc"].saveAs(str(FCSTD_PATH))
    print("Built lower base in", FCSTD_PATH)
