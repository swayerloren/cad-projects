# CAD Workflow

## Use OpenSCAD When

- The part is parametric, code-driven, and mostly mechanical.
- The work needs repeatable holes, ribs, bosses, brackets, enclosures, PCB carriers, clips, or mount patterns.
- Production and preview modes can be cleanly separated.
- STL output is the final manufacturing target.
- The geometry can be expressed clearly with primitives, boolean operations, hulls, and reusable modules.

OpenSCAD production rules:

- Keep preview helpers out of exported STL.
- Use explicit production mode for export.
- Keep reusable modules under the project or `Shared Modules\OpenSCAD`.
- Record parameters in project memory under `CODEX\PROJECTS\<PROJECT>\OPENSCAD_PARAMETERS.md`.

## Use FreeCAD When

- The part needs STEP output, solid CAD history, sketches, constraints, fillets, chamfers, or assemblies.
- The geometry benefits from FreeCAD workbenches, parametric sketches, or richer surface control.
- The project needs imported STEP/STL reference inspection.
- A Python macro can automate repeated geometry, export, validation, or measurements.

FreeCAD install path:

```text
C:\Program Files\FreeCAD 1.1\bin
```

Store reusable FreeCAD code in:

```text
Shared Modules\FreeCAD
tools\FreeCAD Macros
```

## Use A Hybrid Workflow When

- OpenSCAD is best for repeatable mechanical structure but FreeCAD is better for final fillets, chamfers, STEP export, or surface cleanup.
- A complex STL needs to be measured or referenced before recreating a clean parametric model.
- A rough OpenSCAD part should become a FreeCAD solid for manufacturing handoff.

Hybrid rule:

- Use OpenSCAD for parametric/code-driven mechanical systems.
- Use FreeCAD for parts needing fillets, STEP output, sketches, constraints, assemblies, or better organic/surface control.
- Use imported STL/mesh reference when recreating complex organic parts.

## STL Reverse Engineering

1. Preserve the original STL/STEP/reference files.
2. Create a project folder under `OpenSCAD Projects` or `FreeCAD Projects` for new work.
3. Store references in the project `reference` folder or root `Shared Assets\STL References` when reusable.
4. Measure critical interfaces first: holes, screw patterns, shafts, hinge axes, wall thicknesses, clearances, and mating faces.
5. Rebuild functional geometry parametrically instead of tracing every mesh artifact.
6. Use FreeCAD when the source has organic surfaces, fillets, lofts, or STEP-friendly requirements.
7. Write lessons to `Training CAD\STL_REVERSE_ENGINEERING`.

## Documentation After Each Task

Update the project memory under `CODEX\PROJECTS\<PROJECT>` with:

- confirmed facts
- source and export paths
- design decisions
- errors and fixes
- OpenSCAD or FreeCAD parameters
- manufacturing notes
- output reviews

Add reusable lessons to `Training CAD` only after converting the project-specific experience into clean, generalized training material.

