# Preview Vs Production Mode

OpenSCAD projects should separate preview helpers from exportable production geometry.

## Preview Mode

Preview mode may include:

- transparent reference volumes
- imported STL references
- clearance blocks
- measurement guides
- exploded or section views
- labels or debug colors

Preview geometry is for review only.

## Production Mode

Production mode must include only exportable geometry.

Production mode must exclude:

- reference STLs
- debug blocks
- transparent clearance volumes
- labels
- measurement markers
- exploded-only transforms

## Required Pattern

Use modules similar to:

```scad
mode = "preview";

module production_geometry() {
    // exportable geometry only
}

module preview_helpers() {
    // non-export helper geometry
}

module main() {
    production_geometry();
    if (mode == "preview") preview_helpers();
}

main();
```

Export STL with `mode = "production"`.

