# Errors and Fixes

## Non-closed custom prism helper

Initial custom `polyhedron()` profile prisms previewed but produced CGAL warnings during export:

`ERROR: The given mesh is not closed!`

Fix:

Use `linear_extrude()` with rotation for XZ profiles extruded along Y. This produced clean exportable solids.

## Grip ribs too bulky

The first rib model used half cylinders. Bounding box matched, but the grip plate volume was about 694 mm3 too high.

Fix:

Extract the actual rib cross-section from the STL and extrude that measured profile along X. Final area and volume matched the original plate closely.

## OpenSCAD render option

`--render` alone did not produce the expected PNG with this OpenSCAD CLI. `--render=1` worked for rendered PNG output.
