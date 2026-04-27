# Pattern: Multi-Part Geared Machine Rebuild

## Recommended Module Set

Use explicit modules for both real parts and assembly helpers:

```scad
module machine_base() {}
module frame() {}
module spur_gear_part() {}
module ring_gear() {}
module shaft() {}
module bearing_block() {}
module cable_guide() {}
module assembly_preview() {}
module exploded_view() {}
module reference_stl(part) {}
module main() {}
```

## Preview Controls

Prefer both string and numeric selectors:

```scad
preview_part = "assembly";
preview_id = -1; // -1 uses preview_part, otherwise numeric part IDs
show_rebuild = true;
show_reference_stl = false;
show_exploded = false;
```

Numeric selectors avoid quoting errors in PowerShell and batch rendering.

## STL Overlay Rule

Do not use imported STL as rebuild geometry. Use it only like this:

```scad
if (show_reference_stl)
    color([1, 0.2, 0, 0.35])
        import("../../files/Original.stl");
```

## Gear Rebuild Rule

At minimum, expose:
- tooth count
- outer diameter
- root diameter
- thickness
- bore diameter
- hub/post dimensions
- clearance/backlash parameter

Exact involute geometry can be swapped in later if mechanical meshing is required.
