# Repo History

## 2026-04-27 Root Restructure

- The CAD workspace root is now `C:\Users\LJ\CAD Projects`.
- Older notes may still reference `C:\Users\LJ\OpenSCAD Projects`; those paths must be verified before use.
- `CODEX` remains the memory and instruction system.
- `Training Openscad` is preserved and is being migrated into `Training CAD`.
- `Training CAD` is now the preferred reusable knowledge library for OpenSCAD, FreeCAD, hybrid CAD, mechanical design, manufacturing, STL reverse engineering, and future AI/local LLM training data.
- OpenSCAD and FreeCAD are both supported under the same CAD root.
- Existing project folders under `my projects`, `pre made traiing models 3d`, and lowercase `tools` may still exist and must not be silently edited, renamed, moved, or deleted.

## Current Migration Stance

- Index first.
- Add templates and memory structure.
- Keep active source folders where they are.
- Move one project at a time only after path references, scripts, exports, and project memory are checked.

## 2026-04-27 FreeCAD Replication Pass

- Created FreeCAD project folders under `C:\Users\LJ\CAD Projects\FreeCAD Projects` for:
  - `racing seat phone stand`
  - `command link`
- Preserved existing OpenSCAD source folders and original STL/reference files.
- Built Racing Seat Phone Stand as a FreeCAD hybrid model with imported STL references and solid rebuilt mechanical features.
- Built COMMAND LINK as a FreeCAD solid CAD enclosure/fit-check model with base, lid, cable gland clearance, PCB placeholder, relay bracket set, and exports.
- Documented both replications in project-local reports, CODEX project memory, and Training CAD case studies.

## 2026-04-27 GitHub Repo Setup

- Prepared `C:\Users\LJ\CAD Projects` to become a GitHub-backed repository.
- Preferred GitHub repo name: `cad-projects`.
- Intended visibility: private.
- Added `.gitignore` policy to track source/memory/docs while ignoring generated CAD exports, renders, venvs, caches, and unnecessary binaries.
- Repository should track CODEX memory, Training CAD, OpenSCAD source, FreeCAD source, macros, shared modules, and project documentation.
- FreeCAD/OpenSCAD applications are external installs and are not stored in the repo.
