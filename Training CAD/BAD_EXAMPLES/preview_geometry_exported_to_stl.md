# Bad Example: Preview Geometry Exported To STL

## Failure Pattern

The printable OpenSCAD assembly directly calls preview/helper modules:

- PCB placeholders
- wire zone markers
- zip-tie path previews
- clearance blocks
- labels
- debug geometry

When the user exports STL, these helpers become part of the production mesh.

## Why It Fails

Preview geometry is not printable product geometry. It can block real parts, confuse slicers, waste material, and hide whether the production part was actually modeled correctly.

## Rule

Every production SCAD file should separate:

- `production_geometry()`
- `preview_helpers()`
- `main()`

Preview helpers must be gated by a mode such as `is_preview`.

