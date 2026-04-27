# FreeCAD Macro Workflow

Use FreeCAD macros when repeated modeling, measurement, export, or validation should be reproducible.

Reusable macro modules belong in:

```text
C:\Users\LJ\CAD Projects\Shared Modules\FreeCAD
```

Runnable macros belong in:

```text
C:\Users\LJ\CAD Projects\tools\FreeCAD Macros
```

## Running Headless

```powershell
& 'C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe' 'C:\Users\LJ\CAD Projects\tools\FreeCAD Macros\example_macro.py'
```

## Macro Standards

- Use named constants for critical dimensions.
- Keep project-specific paths near the top of the macro.
- Write exports to project-local `exports` folders unless intentionally using root `Exports`.
- Record macro entry points in `CODEX\PROJECTS\<PROJECT>\PATHS.md`.
- Record parameters in `CODEX\PROJECTS\<PROJECT>\FREECAD_PARAMETERS.md`.

Do not hide design decisions inside unnamed feature creation code.

