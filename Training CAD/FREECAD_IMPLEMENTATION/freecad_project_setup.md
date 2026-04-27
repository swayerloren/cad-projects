# FreeCAD Project Setup

Preferred new FreeCAD project root:

```text
C:\Users\LJ\CAD Projects\FreeCAD Projects
```

FreeCAD install path:

```text
C:\Program Files\FreeCAD 1.1\bin
```

## Suggested Project Layout

```text
Project Name\
    README.md
    source\
    reference\
    macros\
    exports\
        STEP\
        STL\
        PNG Renders\
        Reports\
```

## Project Memory

Create matching memory under:

```text
C:\Users\LJ\CAD Projects\CODEX\PROJECTS\<PROJECT>
```

Use:

- `FACTS.md`
- `INSTRUCTIONS.md`
- `DESIGN_DECISIONS.md`
- `ERRORS_AND_FIXES.md`
- `FREECAD_PARAMETERS.md`
- `MANUFACTURING_NOTES.md`
- `PATHS.md`
- `OUTPUT_REVIEWS.md`

## Modeling Notes

- Name sketches, bodies, and important features.
- Keep constraints intentional and documented.
- Record assumptions when deriving dimensions from STL or photos.
- Use STEP exports for solid CAD handoff when needed.
- Keep mesh imports as references unless the project is explicitly mesh-based.

