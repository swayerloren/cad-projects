# STL To Parametric Or Hybrid Model

The goal is not to copy triangles. The goal is to recover a clean, editable CAD model.

## Decide The Target Workflow

Use OpenSCAD when:

- geometry is mostly mechanical and repeatable
- features are holes, bosses, brackets, ribs, gears, clips, or enclosures
- STL output is enough

Use FreeCAD when:

- the part needs sketches, constraints, fillets, chamfers, STEP, assemblies, or surface control
- the source has organic styling or complex blends

Use hybrid workflow when:

- OpenSCAD can rebuild the functional mechanical skeleton
- FreeCAD can finish solids, fillets, surfaces, or STEP export

## Required Notes

Record:

- original source STL paths
- reference photos
- measured dimensions
- assumptions
- accuracy review
- rejected approximations
- final export paths

Store project-specific notes in `CODEX\PROJECTS`. Store reusable lessons in `Training CAD`.

