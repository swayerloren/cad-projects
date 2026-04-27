# Parameter Strategy

Good OpenSCAD files make important dimensions explicit. Parameters are the contract between source facts, design intent, manufacturing assumptions, and future tuning.

## Separate Types Of Values

### Source Facts

Source facts come from drawings, PCB files, CAD files, datasheets, or measurements. They should be near the top and changed only when the source changes.

```scad
pcb_width = 65.000;
pcb_length = 78.710;
pcb_thickness = 1.600;
mounting_hole_positions = [
    [2.600, 2.900],
    [62.190, 2.900],
    [2.600, 75.500],
    [62.190, 75.500]
];
```

### Design Assumptions

Assumptions are values selected by the designer. They should be named clearly and documented.

```scad
wall_thickness = 3.5;
floor_thickness = 4.0;
standoff_height = 5.0;
insert_hole_diameter = 4.2;
```

### Feature Parameters

Counts, spacing, clearances, heights, spans, and diameters must be parameters.

```scad
zip_tie_count_per_side = 6;
zip_tie_y_positions = [11, 22, 33, 44, 55, 66];
zip_tie_tunnel_clear_width = 5.5;
zip_tie_tunnel_clear_height = 3.0;
zip_tie_clearance_from_pcb_edge = 5.0;
```

### Preview Toggles

Preview helpers should be parameterized so they can be turned on during review and off for production views.

```scad
show_pcb_placeholder = true;
show_zip_tie_path_preview = true;
show_wire_bundle_preview = true;
show_service_clearance_preview = true;
```

### Derived Values

Derived dimensions should be calculated once and reused.

```scad
pcb_origin_x = carrier_margin_left;
pcb_origin_y = carrier_margin_front;
body_width = carrier_margin_left + pcb_width + carrier_margin_right;
body_length = carrier_margin_front + pcb_length + carrier_margin_back;
```

## Bad Parameter Practices

- Magic numbers inside `translate()`.
- Hard-coded hole diameters inside cut modules.
- Editing geometry by changing random numbers buried in modules.
- Mixing PCB source dimensions with enclosure assumptions.
- Repeating the same derived formula in multiple places.
- Using vague names such as `d1`, `offset2`, or `thing_h`.

## Review Rule

If a dimension affects fit, strength, serviceability, or manufacturing, it should be a named parameter or derived from named parameters.
