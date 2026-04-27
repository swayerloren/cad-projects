# Training CAD

This is the reusable CAD training library for OpenSCAD, FreeCAD, general mechanical design, manufacturing notes, 3D printing, injection molding, STL reverse engineering, PCB enclosures, wire management, heat-set inserts, brackets, mounts, and future AI/local LLM training data.

It is separate from active project memory:

```text
C:\Users\LJ\CAD Projects\CODEX
```

`CODEX` stores active project facts, instructions, decisions, errors, paths, parameters, and task history.

`Training CAD` stores cleaned lessons, generalized design patterns, examples, reusable implementation notes, reusable modules/macros, prompt templates, and curated datasets.

Do not dump messy logs here. Convert project experience into clean reusable training material first.

## Main Implementation Layers

- `OPENSCAD_IMPLEMENTATION` teaches code-driven parametric CAD methods, module structure, production/preview separation, boolean strategy, render testing, and export discipline.
- `FREECAD_IMPLEMENTATION` teaches FreeCAD project setup, sketch/constraint workflow, macro automation, STEP-oriented work, and FreeCAD-specific modeling habits.
- `STL_REVERSE_ENGINEERING` teaches how to use original meshes and references to rebuild clean parametric geometry.
- `SURFACE_MODELING` documents when OpenSCAD is not the right tool and when FreeCAD or another surface/solid workflow is needed.
- `MANUFACTURING_NOTES` captures design-for-manufacture lessons for FDM, resin, CNC, and injection molding.

Use this library for reusable lessons. Keep project-specific facts in `CODEX\PROJECTS`.
