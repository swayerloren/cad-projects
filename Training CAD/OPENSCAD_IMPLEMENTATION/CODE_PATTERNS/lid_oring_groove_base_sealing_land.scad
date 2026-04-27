// Lid O-ring groove plus base sealing land pattern.
// This is a simplified pattern; validate actual O-ring compression by printing.

oring_cross_section_diameter = 2.0;
oring_groove_width = 2.6;
oring_groove_depth = 1.4;
base_sealing_land_width = 3.2;
base_sealing_land_height = 0.8;
corner_radius = 4.0;

module rounded_box_2d(w, d, r) {
    rr = max(0.01, min(r, min(w, d) / 2 - 0.01));
    hull()
        for (x = [rr, w - rr])
            for (y = [rr, d - rr])
                translate([x, y]) circle(r = rr);
}

module rounded_ring_2d(outer_w, outer_d, ring_w, outer_r, inner_r) {
    difference() {
        rounded_box_2d(outer_w, outer_d, outer_r);
        translate([ring_w, ring_w])
            rounded_box_2d(outer_w - 2 * ring_w, outer_d - 2 * ring_w, inner_r);
    }
}

module lid_oring_groove_cut(body_w, body_l, outer_inset = 0.8) {
    translate([outer_inset, outer_inset, -0.05])
        linear_extrude(height = oring_groove_depth + 0.1)
            rounded_ring_2d(
                body_w - 2 * outer_inset,
                body_l - 2 * outer_inset,
                oring_groove_width,
                corner_radius,
                max(0.6, corner_radius - oring_groove_width)
            );
}

module base_sealing_land(body_w, body_l, top_z, outer_inset = 0.5) {
    translate([outer_inset, outer_inset, top_z])
        linear_extrude(height = base_sealing_land_height)
            rounded_ring_2d(
                body_w - 2 * outer_inset,
                body_l - 2 * outer_inset,
                base_sealing_land_width,
                corner_radius,
                max(0.6, corner_radius - base_sealing_land_width)
            );
}
