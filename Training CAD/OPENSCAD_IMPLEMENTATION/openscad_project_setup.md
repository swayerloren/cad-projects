# OpenSCAD Project Setup

Preferred new OpenSCAD project root:

```text
C:\Users\LJ\CAD Projects\OpenSCAD Projects
```

## Suggested Project Layout

```text
Project Name\
    README.md
    scad\
    reference\
    exports\
        STL\
        PNG Renders\
        Reports\
```

Small projects may keep `.scad` files at the project root if that is clearer.

## Source Rules

- Keep reusable modules in project source until they are stable.
- Promote shared modules to `Shared Modules\OpenSCAD`.
- Separate preview helpers from production geometry.
- Use production mode for STL export.
- Avoid organic surface modeling when OpenSCAD is the wrong tool.
- Record project parameters in `CODEX\PROJECTS\<PROJECT>\OPENSCAD_PARAMETERS.md`.

## Export Rules

- Use project-local `exports`.
- Keep root `Exports` optional.
- Export only production geometry.
- Store render reviews in project memory.

