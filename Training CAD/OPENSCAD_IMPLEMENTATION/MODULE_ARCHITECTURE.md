# Module Architecture

A production-ready OpenSCAD file should be organized so fixed facts, design assumptions, geometry modules, cutouts, previews, and final assembly are easy to inspect.

## Recommended Order

1. Header / purpose
2. Source facts
3. Adjustable design parameters
4. Preview toggles
5. Derived dimensions
6. Helper functions
7. Helper modules
8. Core body modules
9. Feature modules
10. Cutout modules
11. Preview modules
12. Main assembly module
13. Final call

## Example Structure

```scad
// Header and coordinate notes.

// Source facts.
pcb_width = 65.000;
pcb_length = 78.710;

// Adjustable parameters.
wall_thickness = 3.5;
insert_hole_diameter = 4.2;

// Preview toggles.
show_pcb_placeholder = true;
show_zip_tie_path_preview = true;

// Derived values.
body_width = carrier_margin_left + pcb_width + carrier_margin_right;

// Helpers.
module rounded_box_2d(w, d, r) { ... }
module rounded_block(size, r) { ... }

// Core body.
module base_body() { ... }
module perimeter_walls() { ... }

// Features.
module pcb_standoffs() { ... }
module grommet_entry() { ... }
module cable_tie_saddles() { ... }
module external_mounts() { ... }

// Cutouts.
module grommet_cut() { ... }
module screw_hole_cuts() { ... }

// Previews.
module pcb_placeholder() { ... }
module zip_tie_path_preview() { ... }

// Main assembly.
module main_assembly() {
    difference() {
        union() {
            base_body();
            perimeter_walls();
            pcb_standoffs();
            cable_tie_saddles();
        }
        grommet_cut();
        screw_hole_cuts();
    }
    if (show_pcb_placeholder) pcb_placeholder();
}

main_assembly();
```

## Rules

- Do not hard-code critical dimensions deep inside modules.
- Keep feature bodies and cut modules separate.
- Keep preview geometry optional.
- Do not leave dead rejected modules in the file.
- Do not stack patches on bad geometry; replace the bad module.
- Make each important module testable alone when practical.
- Give modules names that describe design intent, not just shape.

## COMMAND LINK Pattern

The current COMMAND LINK rugged enclosure uses this architecture:

- helper geometry
- base / enclosure body
- PCB mounting
- wire entry
- wire retention
- external mounts
- preview and future placeholders
- main assembly

That structure is preferred over a long unsectioned file because each design concern can be edited without disturbing unrelated geometry.
