# CAD Root Audit

Audit date: 2026-04-27

Root audited:

```text
C:\Users\LJ\CAD Projects
```

## Initial Root Folders Found

Before new target folders were added, the root contained:

- `CODEX`
- `my projects`
- `pre made traiing models 3d`
- `tools`
- `Training Openscad`

After alignment, the root also contains:

- `Archive`
- `Exports`
- `FreeCAD Projects`
- `OpenSCAD Projects`
- `Shared Assets`
- `Shared Modules`
- `Training CAD`

## CODEX Status

- `CODEX` exists.
- `CODEX\PROJECTS` exists.
- Global instruction files found:
  - `CODEX\GLOBAL_INSTRUCTIONS.md`
  - `CODEX\MECHANICAL_DESIGN_STANDARDS.md`
  - `CODEX\README.md`
- Project memory folders found:
  - `CABLE_WRAPPING_MACHINE_6725750`
  - `COMMAND_LINK`
  - `CRANE_ARM_PHONE_MOUNT`
  - `FOOT_PEDAL_SWITCH`
  - `RACING_SEAT_PHONE_STAND`

## Training Openscad Status

- `Training Openscad` exists and was not deleted.
- It contains reusable OpenSCAD training material, including good examples, bad examples, design rules, manufacturing notes, OpenSCAD implementation notes, OpenSCAD modules, PCB carrier lessons, prompt templates, and wire management notes.
- Its reusable content was copied/indexed into `Training CAD`.
- Migration note created at `Training Openscad\MIGRATED_TO_TRAINING_CAD.md`.

## tools/.venv Status

- Existing venv path: `tools\.venv`
- Python version from `pyvenv.cfg`: `3.12.10`
- `include-system-site-packages`: `false`
- Installed packages observed:
  - `contourpy==1.3.3`
  - `cycler==0.12.1`
  - `fonttools==4.62.1`
  - `kiwisolver==1.5.0`
  - `matplotlib==3.10.9`
  - `numpy==2.4.4`
  - `packaging==26.2`
  - `pandas==3.0.2`
  - `pillow==12.2.0`
  - `pip==26.0.1`
  - `pyparsing==3.3.2`
  - `python-dateutil==2.9.0.post0`
  - `sexpdata==1.0.2`
  - `six==1.17.0`
  - `tzdata==2026.2`
- `tools\output` exists and is preserved.
- `pyvenv.cfg` records the venv creation command using an older path under `C:\Users\LJ\OpenSCAD Projects\command link\tools\.venv`; document this as historical metadata, not the current root.

## FreeCAD Path Status

FreeCAD path exists:

```text
C:\Program Files\FreeCAD 1.1\bin
```

FreeCAD executables found include:

- `freecad.exe`
- `freecadcmd.exe`
- `python.exe`

## OpenSCAD Project Folders Found

- `my projects\command link\openscad_pcb_carrier`
- `my projects\Essenx mini pc mount`
- `my projects\iPhone 17 Pro Max MOLLE Phone Armor`
- `pre made traiing models 3d\Cable Wrapping Machine - 6725750\openscad_rebuild`
- `pre made traiing models 3d\crane arm phone mount\openscad_rebuild`
- `pre made traiing models 3d\foot pedal SWITCH\openscad_rebuild`
- `pre made traiing models 3d\racing seat phone stand\openscad_rebuild`
- `pre made traiing models 3d\racing seat phone stand\openscad_rebuild_v2`
- `pre made traiing models 3d\racing seat phone stand\openscad_rebuild_v3`
- `pre made traiing models 3d\semi-automatic-cable-wrapper-model_files\openscad_rebuild`

## FreeCAD Project Folders Found

No `.FCStd` project folders were found.

Potential FreeCAD/STEP reference material found:

- `pre made traiing models 3d\WE-R2.4+Six-Axis+Robot+Arm\arm.STEP`
- `pre made traiing models 3d\semi-automatic-cable-wrapper-model_files\Semi-automatic cable wrapper v14.step`

## Exports And Output Folders Found

- `Exports`
- `my projects\command link\openscad_pcb_carrier\exports`
- `my projects\iPhone 17 Pro Max MOLLE Phone Armor\exports`
- `pre made traiing models 3d\Cable Wrapping Machine - 6725750\openscad_rebuild\exports`
- `pre made traiing models 3d\crane arm phone mount\openscad_rebuild\exports`
- `pre made traiing models 3d\foot pedal SWITCH\openscad_rebuild\exports`
- `pre made traiing models 3d\racing seat phone stand\openscad_rebuild\exports`
- `pre made traiing models 3d\racing seat phone stand\openscad_rebuild_v2\exports`
- `pre made traiing models 3d\racing seat phone stand\openscad_rebuild_v3\exports`
- `pre made traiing models 3d\semi-automatic-cable-wrapper-model_files\openscad_rebuild\exports`
- `tools\output`
- `tools\Analysis Output`

## Duplicate Or Old Naming Issues

- `Training Openscad` is the old OpenSCAD-specific training folder. `Training CAD` is now the preferred reusable training folder.
- `tools` exists with lowercase physical casing. The requested `Tools` path resolves to the same folder on Windows. Do not rename it silently.
- `my projects` contains active projects but new OpenSCAD work should normally go under `OpenSCAD Projects`.
- `pre made traiing models 3d` contains a misspelled legacy name and should stay in place until a deliberate migration plan is approved.

## Migration Risks

- Moving active project source folders could break existing references, scripts, render/export paths, and CODEX project-memory links.
- Renaming `tools` to `Tools` could invalidate scripts or documentation that use the lowercase path, even though Windows path lookup is case-insensitive.
- Moving `Training Openscad` before validating copied content could lose historical training context.
- Moving STL reference libraries can break reverse-engineering notes and screenshots that point to old paths.

