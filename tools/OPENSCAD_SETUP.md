# OpenSCAD Setup

OpenSCAD projects should normally live under:

```text
C:\Users\LJ\CAD Projects\OpenSCAD Projects
```

Existing OpenSCAD work remains in legacy/current folders until deliberately migrated.

## Where Scripts Belong

Reusable OpenSCAD modules:

```text
C:\Users\LJ\CAD Projects\Shared Modules\OpenSCAD
```

Reusable OpenSCAD automation scripts:

```text
C:\Users\LJ\CAD Projects\tools\OpenSCAD Scripts
```

Project-specific `.scad` files should stay inside the project folder.

## Export Rules

- Use project-local `exports` folders for active work.
- Use root `Exports` only as an optional shared or final output mirror.
- Keep preview helpers out of production STL.
- Use production mode for exported STL.
- Record parameters in `CODEX\PROJECTS\<PROJECT>\OPENSCAD_PARAMETERS.md`.

