// First-pass printed lid O-ring groove pattern.

$fn = 48;

body_width = 95.8;
body_length = 98.71;
lid_top_thickness = 3.5;
lid_corner_radius = 4;

oring_cross_section_diameter = 2.0;
oring_groove_width = 2.6;
oring_groove_depth = 1.4;
oring_groove_outer_inset = 0.8;

module rounded_box_2d(w, d, r) {
    rr = max(0.01, min(r, min(w, d) / 2 - 0.01));
    hull() {
        for (x = [rr, w - rr])
            for (y = [rr, d - rr])
                translate([x, y])
                    circle(r = rr);
    }
}

module rounded_ring_2d(outer_w, outer_d, ring_w, outer_r, inner_r) {
    difference() {
        rounded_box_2d(outer_w, outer_d, outer_r);
        translate([ring_w, ring_w])
            rounded_box_2d(
                outer_w - 2 * ring_w,
                outer_d - 2 * ring_w,
                inner_r
            );
    }
}

module lid_panel() {
    linear_extrude(height = lid_top_thickness)
        rounded_box_2d(body_width, body_length, lid_corner_radius);
}

module oring_groove_cut() {
    translate([oring_groove_outer_inset, oring_groove_outer_inset, -0.05])
        linear_extrude(height = oring_groove_depth + 0.10)
            rounded_ring_2d(
                body_width - 2 * oring_groove_outer_inset,
                body_length - 2 * oring_groove_outer_inset,
                oring_groove_width,
                lid_corner_radius,
                max(0.6, lid_corner_radius - oring_groove_width)
            );
}

difference() {
    lid_panel();
    oring_groove_cut();
}
