# Production SCAD File Template

Use this skeleton for production-refinement OpenSCAD files.

```scad
// Project / part name.
// Purpose:
// Source references:
// Coordinate system:

$fn = 48;

// ---------------------------------------------------------------------------
// Source facts
// ---------------------------------------------------------------------------

pcb_width = 0;
pcb_length = 0;
pcb_thickness = 1.6;
mounting_hole_positions = [];

// ---------------------------------------------------------------------------
// Adjustable design parameters
// ---------------------------------------------------------------------------

wall_thickness = 3.0;
floor_thickness = 4.0;
tolerance = 0.5;

// ---------------------------------------------------------------------------
// Preview toggles
// ---------------------------------------------------------------------------

show_pcb_placeholder = true;
show_clearance_preview = true;

// ---------------------------------------------------------------------------
// Derived dimensions
// ---------------------------------------------------------------------------

pcb_origin_x = carrier_margin_left;
pcb_origin_y = carrier_margin_front;
body_width = carrier_margin_left + pcb_width + carrier_margin_right;
body_length = carrier_margin_front + pcb_length + carrier_margin_back;

function pcb_x(x) = pcb_origin_x + x;
function pcb_y(y) = pcb_origin_y + y;

// ---------------------------------------------------------------------------
// Helper functions and modules
// ---------------------------------------------------------------------------

module rounded_box_2d(w, d, r) { /* ... */ }
module rounded_block(size, r) { /* ... */ }

// ---------------------------------------------------------------------------
// Base body
// ---------------------------------------------------------------------------

module base_body() { /* floor */ }
module perimeter_walls() { /* walls */ }

// ---------------------------------------------------------------------------
// Holes and cutouts
// ---------------------------------------------------------------------------

module grommet_cut() { /* through-wall circular cut */ }
module screw_hole_cuts() { /* screw holes */ }

// ---------------------------------------------------------------------------
// Feature modules
// ---------------------------------------------------------------------------

module pcb_standoffs() { /* standoffs with insert holes */ }
module cable_tie_saddles() { /* strain relief */ }
module external_mounts() { /* mounting ears */ }

// ---------------------------------------------------------------------------
// Preview modules
// ---------------------------------------------------------------------------

module pcb_placeholder() { /* translucent PCB */ }
module service_clearance_preview() { /* translucent clearance */ }

// ---------------------------------------------------------------------------
// Main assembly
// ---------------------------------------------------------------------------

module main_assembly() {
    difference() {
        union() {
            base_body();
            perimeter_walls();
            pcb_standoffs();
            cable_tie_saddles();
            external_mounts();
        }
        grommet_cut();
        screw_hole_cuts();
    }

    if (show_pcb_placeholder)
        pcb_placeholder();
}

main_assembly();
```

## Template Rules

- Every feature should have parameters.
- Every cut should have a named cut module.
- Preview helpers should be separate from production geometry.
- Source facts should not be mixed with design assumptions.
- Final assembly should be readable in one screen.
