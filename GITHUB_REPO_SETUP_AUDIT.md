# GitHub Repo Setup Audit

Audit date: 2026-04-27

Root:

```text
C:\Users\LJ\CAD Projects
```

## Tool Status

| Check | Result |
|---|---|
| Git available | yes, `git version 2.52.0.windows.1` |
| GitHub CLI available | yes, `gh version 2.89.0` |
| GitHub CLI authenticated | yes, authenticated to `github.com` as `swayerloren` |
| Existing `.git` folder | no |
| Current branch | none before initialization |
| Current remotes | none before initialization |

## Size Audit

Estimated total root size before ignore rules:

```text
571.15 MB
```

Largest folders:

| Folder | Approx Size |
|---|---:|
| `pre made traiing models 3d` | 323.12 MB |
| `tools` | 186.08 MB |
| `my projects` | 51.04 MB |
| `FreeCAD Projects` | 10.19 MB |
| `Training CAD` | 0.26 MB |
| `Training Openscad` | 0.24 MB |
| `CODEX` | 0.20 MB |

## Large Files Found

Large files are mostly STL/STEP references, generated exports, and venv libraries. Examples:

- `pre made traiing models 3d\pilotseat_stls\obj_1_quant_1.stl` about 38 MB
- `pre made traiing models 3d\WE-R2.4+Six-Axis+Robot+Arm\arm.STEP` about 38 MB
- `pre made traiing models 3d\semi-automatic-cable-wrapper-model_files\Counterweighted Gear.stl` about 30 MB
- `tools\.venv\Lib\site-packages\...\*.dll` and `*.pyd` files
- OpenSCAD and FreeCAD generated export folders

## Files That Should Be Ignored

- Python virtual environments and caches
- `tools\output`
- generated CAD exports under `exports` / `Exports`
- generated mesh/solid export files: STL, OBJ, 3MF, STEP, STP, IGES, IGS, DXF
- generated renders/photos/images: PNG, JPG, JPEG, AVIF, WEBP, GIF
- PDFs unless explicitly approved
- FreeCAD backup/cache files
- OpenSCAD backup/cache/log files
- OS/editor junk

## Files Safe To Commit

- root documentation
- `.gitignore`
- `CODEX` memory and project memory files
- `Training CAD` markdown, JSONL, SCAD examples, and text datasets
- `OpenSCAD Projects` templates and `.scad` source files
- `FreeCAD Projects` macros, docs, and reasonably sized `.FCStd` source files
- `Shared Modules`
- `Shared Assets` docs and lightweight text references
- `tools` docs and source scripts, excluding venv/output folders

## Pre-Create Decision

It is safe to initialize Git after creating `.gitignore`, then stage only source/documentation/template folders and verify staged files before commit.

