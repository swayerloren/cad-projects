# CAD Projects

CAD project workspace for OpenSCAD, FreeCAD, CODEX memory, Training CAD, shared modules, reusable tools, and mechanical design documentation.

Root path:

```text
C:\Users\LJ\CAD Projects
```

## What This Repo Tracks

| Folder | Purpose |
|---|---|
| `CODEX` | Repo memory, global instructions, design standards, active project index, facts, decisions, errors, and per-project notes. |
| `Training CAD` | Reusable CAD lessons across OpenSCAD, FreeCAD, mechanical design, manufacturing, 3D printing, STL reverse engineering, PCB enclosures, wire management, inserts, brackets, and mounts. |
| `OpenSCAD Projects` | Preferred home for new OpenSCAD source projects unless the user gives a different path. |
| `FreeCAD Projects` | Preferred home for new FreeCAD source projects unless the user gives a different path. |
| `Shared Modules` | Reusable OpenSCAD modules, FreeCAD scripts/macros, and Python helpers shared across projects. |
| `Shared Assets` | Reference photos, STL references, hardware dimensions, datasheets, and other non-project-specific assets. |
| `Exports` | Optional root-level landing area for generated outputs. Most generated exports are ignored by Git. |
| `tools` / `Tools` | Existing tools folder. On Windows this resolves to the requested `Tools` path; the physical folder currently uses lowercase `tools`. |
| `Archive` | Parking area for retired material after explicit migration decisions. |

## Key Docs

- [CAD_PROJECTS_INDEX.md](CAD_PROJECTS_INDEX.md)
- [CAD_WORKFLOW.md](CAD_WORKFLOW.md)
- [FOLDER_STRUCTURE.md](FOLDER_STRUCTURE.md)
- [MIGRATION_PLAN.md](MIGRATION_PLAN.md)
- [CAD_ROOT_AUDIT.md](CAD_ROOT_AUDIT.md)
- [CAD_ROOT_VALIDATION.md](CAD_ROOT_VALIDATION.md)

## How To Use This Repo

1. Read `CODEX\REPO_MEMORY.md` and `CODEX\GLOBAL_INSTRUCTIONS.md` before changing CAD work.
2. Use `CODEX\PROJECTS\<PROJECT>` for project-specific memory, facts, decisions, errors, and paths.
3. Put reusable lessons in `Training CAD`.
4. Put new OpenSCAD projects under `OpenSCAD Projects`.
5. Put new FreeCAD projects under `FreeCAD Projects`.
6. Keep generated exports in project-local `exports` folders or root `Exports`.

## Export And Binary Policy

Generated exports are mostly ignored by default:

- STL / OBJ / 3MF
- STEP / STP / IGES / IGS
- DXF
- PNG/JPG/AVIF/WEBP/GIF renders and photos
- PDFs
- virtual environments, caches, and tool output folders

FreeCAD source files (`.FCStd`) are not ignored by default. Track them when they are reasonably sized and represent source CAD, not disposable exports or backups.

Large reference meshes, generated render sets, and binary manufacturing exports should only be committed intentionally.

## External Apps

FreeCAD and OpenSCAD are installed outside this repo. This repository stores source files, macros, project memory, and documentation, not the CAD applications themselves.

Do not silently edit similarly named folders. Verify the exact target path before changing CAD source, project memory, training material, or generated exports.

Key repo memory files:

- `CODEX\REPO_MEMORY.md`
- `CODEX\REPO_HISTORY.md`
- `CODEX\ACTIVE_PROJECTS.md`
