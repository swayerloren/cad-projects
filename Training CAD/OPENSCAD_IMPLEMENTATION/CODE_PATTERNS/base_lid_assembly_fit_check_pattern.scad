// Pattern: base/lid assembly fit check using production STL imports.

include <shared_dimensions.scad>

fit_mode = "closed"; // "closed", "exploded", "cutaway", "alignment"

show_oring_preview = true;
show_fastener_alignment = true;
show_clearance_envelopes = true;

base_stl_path = "exports/base_production.stl";
lid_stl_path = "exports/lid_production.stl";

lid_closed_z = base_lid_seat_z();
lid_z = (fit_mode == "exploded") ? lid_closed_z + 30 : lid_closed_z;

module base_import() {
    color([0.45, 0.45, 0.45, 0.75])
        import(base_stl_path, convexity = 10);
}

module lid_import() {
    translate([0, 0, lid_z])
        color([0.1, 0.1, 0.12, 0.6])
            import(lid_stl_path, convexity = 10);
}

module fastener_alignment_preview() {
    if (show_fastener_alignment)
        for (p = lid_fastener_positions())
            %translate([p[0], p[1], 0])
                cylinder(h = lid_closed_z + 10, d = screw_clearance_diameter);
}

module main() {
    if (fit_mode == "cutaway") {
        difference() {
            union() {
                base_import();
                lid_import();
            }
            translate([body_width() / 2, -20, -5])
                cube([body_width(), body_length() + 40, lid_closed_z + 20]);
        }
    } else {
        base_import();
        lid_import();
    }

    fastener_alignment_preview();
}

main();
