# FreeCAD Macro Project Workflow

Use a macro workflow when FreeCAD modeling, measurement, or export needs to be repeatable.

## Recommended Folders

Reusable macro code:

```text
C:\Users\LJ\CAD Projects\Shared Modules\FreeCAD
```

Runnable macros:

```text
C:\Users\LJ\CAD Projects\tools\FreeCAD Macros
```

Project macros:

```text
FreeCAD Projects\<PROJECT>\freecad\macros
```

## Workflow

1. Define named dimensions near the top of the macro or in a small parameter module.
2. Build named sketches, bodies, and features.
3. Recompute after major feature groups.
4. Export STEP for solid CAD handoff when needed.
5. Export STL only after confirming tessellation settings and units.
6. Record macro entry points in `CODEX\PROJECTS\<PROJECT>\PATHS.md`.
7. Record parameters in `CODEX\PROJECTS\<PROJECT>\FREECAD_PARAMETERS.md`.

Run headless with:

```powershell
& 'C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe' 'path\to\macro.py'
```

