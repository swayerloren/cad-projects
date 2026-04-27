# FreeCAD Project Template

FreeCAD install path:

```text
C:\Program Files\FreeCAD 1.1\bin
```

## When To Use FreeCAD Instead Of OpenSCAD

Use FreeCAD for:

- sketches and constraints
- fillets and chamfers
- STEP/solid CAD deliverables
- assemblies
- imported STEP/STL reference inspection
- surface-heavy or organic shape control

Use OpenSCAD for simpler parametric mechanical geometry and repeatable code-driven STL output.

## Run FreeCAD

```powershell
& 'C:\Program Files\FreeCAD 1.1\bin\freecad.exe'
```

## Run Macros

Headless FreeCAD command:

```powershell
& 'C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe' 'freecad\macros\build_model.py'
```

## Export Workflow

- STEP exports go to `exports\STEP`.
- STL exports go to `exports\STL`.
- PNG renders go to `exports\PNG`.
- Reports and review notes go to `exports\Reports` and `docs`.

`freecad\main.FCStd` is a placeholder in the template. Replace it with a real FreeCAD document when starting a project.

Create a matching CODEX project memory folder before active work.

