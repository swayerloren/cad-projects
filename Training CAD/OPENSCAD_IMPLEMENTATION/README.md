# OpenSCAD Implementation

This folder teaches how to implement mechanical design intent in OpenSCAD.

It complements the design-rule folders by focusing on code structure, coordinate mapping, boolean logic, tunnels, preview helpers, render testing, and serviceability validation.

Use these files when a future AI or human needs to understand not just what a part should do, but how the OpenSCAD geometry should be built so the part is physically real and testable.

## Contents

- `MODULE_ARCHITECTURE.md` - recommended production SCAD file organization.
- `PARAMETER_STRATEGY.md` - source facts, assumptions, derived values, and preview toggles.
- `COORDINATE_SYSTEMS.md` - PCB-local to enclosure coordinate mapping.
- `BOOLEAN_OPERATIONS.md` - practical `union()`, `difference()`, `intersection()`, and cutout rules.
- `TUNNELS_SLOTS_AND_CUTOUTS.md` - real pass-through geometry for slots and tie tunnels.
- `PREVIEW_AND_DEBUG_HELPERS.md` - translucent placeholders and debug geometry.
- `SERVICEABILITY_CHECKS.md` - assembly-aware CAD checks.
- `COMMON_OPENSCAD_FAILURES.md` - frequent modeling and render failures.
- `OPENSCAD_RENDER_TESTING.md` - F5/F6, STL export, and coupon testing guidance.
- `PRODUCTION_SCAD_FILE_TEMPLATE.md` - recommended SCAD skeleton.
- `CODE_PATTERNS/` - small renderable OpenSCAD examples.
- `CASE_STUDIES/` - COMMAND LINK implementation lessons.
