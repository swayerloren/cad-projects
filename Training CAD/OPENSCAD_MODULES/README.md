# OpenSCAD Modules

This folder stores reusable educational OpenSCAD modules.

Each module folder should include:

- `README.md`
- A `.scad` example
- `lesson.md`

Modules are examples, not guaranteed production-ready parts.

For implementation-level explanations of how modules should be structured, how cutouts should be made, and how to test renderability, see:

```text
OPENSCAD_IMPLEMENTATION
```

Reusable module folders should link back to implementation patterns when the module depends on a specific OpenSCAD technique such as `difference()` tunnel cuts, hull-based rounded lugs, or preview-only clearance geometry.
