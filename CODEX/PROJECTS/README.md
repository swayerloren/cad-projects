# Project Knowledge Folders

Each project under this folder stores Codex memory for one CAD project.

This is memory, not source CAD. Do not move CAD files here unless explicitly instructed.

Use `PROJECT_TEMPLATE` when creating a new project memory folder.

Standard files:

- `README.md`
- `FACTS.md`
- `INSTRUCTIONS.md`
- `LIVE_WORKING_MEMORY.md`
- `SESSION_HISTORY.md`
- `DESIGN_DECISIONS.md`
- `ERRORS_AND_FIXES.md`
- `DO_AND_DONT.md`
- `OPENSCAD_PARAMETERS.md`
- `FREECAD_PARAMETERS.md`
- `MANUFACTURING_NOTES.md`
- `TODO.md`
- `OUTPUT_REVIEWS.md`
- `PATHS.md`

Before editing any source or export, verify the exact target path in `PATHS.md` or add it if missing.

OpenSCAD source should normally live under `OpenSCAD Projects`. FreeCAD source should normally live under `FreeCAD Projects`. Existing legacy project folders may remain in place until deliberately migrated.
