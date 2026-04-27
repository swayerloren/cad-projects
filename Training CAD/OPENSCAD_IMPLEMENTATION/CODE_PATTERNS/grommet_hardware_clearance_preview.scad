// Grommet hardware clearance preview pattern.
// Preview helpers must be outside production geometry and gated by mode.

mode = "preview";
is_preview = mode == "preview";

hole_d = 16;
wall_t = 3.5;
outer_flange_d = 24;
inner_flange_d = 24;
flange_t = 3;
wire_bundle_d = 8;
wire_bend_r = 24;

show_grommet_hardware_preview = true;
show_wire_bend_clearance_preview = true;

module preview_ring(d_outer, d_inner, h) {
    difference() {
        cylinder(h = h, d = d_outer);
        translate([0, 0, -0.02])
            cylinder(h = h + 0.04, d = d_inner);
    }
}

module grommet_hardware_preview() {
    if (is_preview && show_grommet_hardware_preview) {
        %color([0, 0.45, 1, 0.25])
            translate([0, -flange_t, 0])
                rotate([-90, 0, 0])
                    preview_ring(outer_flange_d, hole_d, flange_t);

        %color([0.1, 0.75, 1, 0.20])
            translate([0, wall_t, 0])
                rotate([-90, 0, 0])
                    preview_ring(inner_flange_d, hole_d, flange_t);
    }
}

module tube_between(p1, p2, d) {
    hull() {
        translate(p1) sphere(d = d);
        translate(p2) sphere(d = d);
    }
}

module wire_bend_preview() {
    if (is_preview && show_wire_bend_clearance_preview)
        %color([0, 0.85, 0.35, 0.24])
            tube_between([0, wall_t, 0], [0, wall_t + wire_bend_r, 0], wire_bundle_d);
}
