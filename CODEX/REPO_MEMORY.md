# Repo Memory

Last updated: 2026-04-27

## CAD Root

```text
C:\Users\LJ\CAD Projects
```

This root supports both OpenSCAD and FreeCAD. Do not assume older `C:\Users\LJ\OpenSCAD Projects` paths are still active.

## Major Folders

| Folder | Purpose |
|---|---|
| `CODEX` | Global memory, instructions, standards, repo history, active project index, and project-specific live memory. |
| `CODEX\PROJECTS` | Per-project memory folders. These are not source CAD folders. |
| `Training CAD` | Reusable lessons, examples, design rules, implementation notes, and future AI/local LLM training data. |
| `OpenSCAD Projects` | Preferred home for new OpenSCAD source projects. |
| `FreeCAD Projects` | Preferred home for new FreeCAD source projects. |
| `Shared Modules` | Reusable OpenSCAD modules, FreeCAD modules/macros, and Python helpers. |
| `Shared Assets` | Reusable photos, STL references, hardware dimensions, and datasheets. |
| `tools` / `Tools` | Existing tool folder with Python venv, FreeCAD macros, OpenSCAD scripts, and analysis outputs. |
| `Exports` | Optional root-level export mirror for STL, STEP, PNG, DXF, and reports. |
| `Archive` | Retired material only after explicit approval. |

## OpenSCAD And FreeCAD

Use OpenSCAD for parametric mechanical geometry, enclosures, holes, ribs, bosses, brackets, PCB carriers, and repeatable STL-producing code.

Use FreeCAD for sketches, constraints, fillets, chamfers, STEP solids, assemblies, surface-heavy work, and macro-driven solid CAD automation.

Use hybrid workflows for organic STL-derived parts or projects where OpenSCAD handles repeatable structure and FreeCAD handles final solid modeling, fillets, or STEP export.

## Where Files Live

- Active source files stay in their project folders.
- New OpenSCAD projects normally go under `OpenSCAD Projects`.
- New FreeCAD projects normally go under `FreeCAD Projects`.
- Existing legacy project folders under `my projects` and `pre made traiing models 3d` remain in place until deliberately migrated.
- Project-specific memory goes under `CODEX\PROJECTS\<PROJECT>`.
- Reusable lessons go under `Training CAD`.
- Reusable code goes under `Shared Modules`.
- Project exports go in project-local export folders; root `Exports` is optional.

## Current Rules Codex Must Remember

- Verify exact active paths before editing.
- Never silently edit similarly named folders.
- Do not delete existing project files.
- Do not delete `Training Openscad`.
- Do not move active projects unless a migration is reviewed and clearly safe.
- Update project memory after meaningful work.
- Add reusable lessons to `Training CAD` when a lesson is broadly useful.
- Before success, verify exact files modified and required structure exists.
- This CAD root is GitHub-backed as private repo `swayerloren/cad-projects` unless renamed.
- Remote URL: `https://github.com/swayerloren/cad-projects.git`.
- Track docs, SCAD, FreeCAD source files, macros, shared modules, CODEX memory, and Training CAD.
- Do not commit generated exports, virtual environments, caches, secrets, or unnecessary large binaries unless explicitly requested.
- FreeCAD and OpenSCAD applications are installed outside this repo and must not be stored here.
- Never commit secrets, tokens, private credentials, or authentication material.
