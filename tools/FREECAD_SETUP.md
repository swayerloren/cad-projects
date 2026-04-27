# FreeCAD Setup

FreeCAD install path:

```text
C:\Program Files\FreeCAD 1.1\bin
```

Executables observed:

```text
C:\Program Files\FreeCAD 1.1\bin\freecad.exe
C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe
C:\Program Files\FreeCAD 1.1\bin\python.exe
```

## Run FreeCAD GUI

```powershell
& 'C:\Program Files\FreeCAD 1.1\bin\freecad.exe'
```

## Run FreeCAD Headless / Macro Scripts

Use `freecadcmd.exe` for scripts that need FreeCAD modules without the GUI:

```powershell
& 'C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe' 'C:\Users\LJ\CAD Projects\tools\FreeCAD Macros\example_macro.py'
```

Use FreeCAD's bundled Python when a script needs the bundled FreeCAD Python environment:

```powershell
& 'C:\Program Files\FreeCAD 1.1\bin\python.exe' 'C:\Users\LJ\CAD Projects\tools\FreeCAD Macros\example_macro.py'
```

## Where FreeCAD Code Belongs

Reusable shared modules:

```text
C:\Users\LJ\CAD Projects\Shared Modules\FreeCAD
```

Runnable macros/scripts:

```text
C:\Users\LJ\CAD Projects\tools\FreeCAD Macros
```

Project-specific FreeCAD source:

```text
C:\Users\LJ\CAD Projects\FreeCAD Projects
```

Record project parameters in `CODEX\PROJECTS\<PROJECT>\FREECAD_PARAMETERS.md`.

