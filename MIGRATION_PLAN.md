# Migration Plan

Date: 2026-04-27

## Current Folders

| Current Folder | Status |
|---|---|
| `CODEX` | Keep. This remains the project memory and instruction store. |
| `Training Openscad` | Preserve. Copied/indexed into `Training CAD`; do not delete. |
| `my projects` | Preserve for now. Contains active OpenSCAD projects. |
| `pre made traiing models 3d` | Preserve for now. Contains STL/STEP references and OpenSCAD rebuilds. |
| `tools` | Preserve for now. Contains the current Python venv, PCB analysis script, requirements, and legacy output. |

## Proposed Final Folders

| Final Folder | Intended Use |
|---|---|
| `OpenSCAD Projects` | New OpenSCAD source projects. |
| `FreeCAD Projects` | New FreeCAD source projects. |
| `Training CAD` | Reusable CAD training material across OpenSCAD, FreeCAD, manufacturing, STL reverse engineering, and mechanical design. |
| `Shared Modules` | Reusable OpenSCAD modules, FreeCAD macros/scripts, and Python helpers. |
| `Shared Assets` | Reusable references, photos, STL references, hardware dimensions, and datasheets. |
| `Exports` | Root-level optional generated output mirror. Project-local exports remain preferred. |
| `tools` / `Tools` | Shared scripts and local tool environments. Physical folder casing is currently lowercase. |
| `Archive` | Retired material only after explicit approval. |

## What Should Move Later

Do not run these automatically. Review first.

- Consider moving `my projects\command link\openscad_pcb_carrier` to `OpenSCAD Projects\COMMAND_LINK` after updating scripts, README paths, and CODEX `PATHS.md`.
- Consider moving `my projects\Essenx mini pc mount` to `OpenSCAD Projects\Essenx mini pc mount`.
- Consider moving `my projects\iPhone 17 Pro Max MOLLE Phone Armor` to `OpenSCAD Projects\iPhone 17 Pro Max MOLLE Phone Armor`.
- Consider indexing STL reference libraries from `pre made traiing models 3d` into `Shared Assets\STL References`, but do not move them until linked notes are updated.
- Consider rebuilding STEP-heavy or surface-heavy projects under `FreeCAD Projects`.

## What Should Stay For Now

- `CODEX`
- `CODEX\PROJECTS`
- `Training Openscad`
- `tools\.venv`
- `tools\output`
- All current active project source folders
- All STL/STEP reference folders

## Risks

- Existing project READMEs and scripts may use hardcoded paths.
- The Python venv has historical creation metadata from an older root path.
- Old folder names include lowercase `tools`, `my projects`, and misspelled `pre made traiing models 3d`.
- Moving many folders at once would make it hard to detect broken references.

## Recommended Next Steps

1. For each active project, create or update `CODEX\PROJECTS\<PROJECT>\PATHS.md`.
2. Move one project at a time only after path references are checked.
3. After each move, run render/export scripts and update project memory.
4. Keep `Training Openscad` until the copied `Training CAD` material has been reviewed.
5. Keep `tools` as-is unless a deliberate case-normalization rename is approved.

## Commands Not To Run Automatically

These are examples of actions that should require explicit approval:

```powershell
Move-Item -LiteralPath 'C:\Users\LJ\CAD Projects\my projects\command link\openscad_pcb_carrier' -Destination 'C:\Users\LJ\CAD Projects\OpenSCAD Projects\COMMAND_LINK'
Rename-Item -LiteralPath 'C:\Users\LJ\CAD Projects\tools' -NewName 'Tools'
Remove-Item -LiteralPath 'C:\Users\LJ\CAD Projects\Training Openscad' -Recurse
```

