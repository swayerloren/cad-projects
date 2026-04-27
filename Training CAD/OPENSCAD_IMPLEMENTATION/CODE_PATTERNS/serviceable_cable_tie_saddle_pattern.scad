// Serviceable cable-tie saddle pattern.
// The tunnel is visible and reachable from above after nearby hardware is installed.

$fn = 36;

zip_tie_band_width = 4.0;
zip_tie_band_thickness = 1.4;
zip_tie_tunnel_clear_width = 5.5;
zip_tie_tunnel_clear_height = 3.0;
zip_tie_bridge_top_height = 7.0;
zip_tie_bridge_thickness = 2.5;
zip_tie_bridge_span = 8.0;
zip_tie_bridge_length_along_y = 7.0;
zip_tie_foot_width = 2.8;
zip_tie_foot_length = 7.0;
show_previews = true;

function saddle_total_width() = zip_tie_bridge_span + 2 * zip_tie_foot_width;

module rounded_rect_2d(w, d, r) {
    rr = max(0.01, min(r, min(w, d) / 2 - 0.01));
    hull() for (x = [rr, w - rr]) for (y = [rr, d - rr])
        translate([x, y]) circle(r = rr);
}

module rounded_block(size, r = 0.8) {
    linear_extrude(height = size[2])
        rounded_rect_2d(size[0], size[1], r);
}

module saddle_tunnel_cut() {
    translate([
        -zip_tie_tunnel_clear_width / 2,
        -zip_tie_foot_length / 2 - 0.35,
        -0.02
    ])
        cube([
            zip_tie_tunnel_clear_width,
            zip_tie_foot_length + 0.7,
            zip_tie_tunnel_clear_height + 0.04
        ]);
}

module serviceable_cable_tie_saddle() {
    total_x = saddle_total_width();
    bridge_bottom = zip_tie_bridge_top_height - zip_tie_bridge_thickness;
    foot_h = max(zip_tie_tunnel_clear_height, bridge_bottom);
    foot_y = max(zip_tie_foot_length, zip_tie_bridge_length_along_y);

    difference() {
        union() {
            translate([-total_x / 2, -foot_y / 2, 0])
                rounded_block([zip_tie_foot_width, foot_y, foot_h], 0.7);
            translate([total_x / 2 - zip_tie_foot_width, -foot_y / 2, 0])
                rounded_block([zip_tie_foot_width, foot_y, foot_h], 0.7);
            translate([-total_x / 2, -zip_tie_bridge_length_along_y / 2, bridge_bottom])
                rounded_block([total_x, zip_tie_bridge_length_along_y, zip_tie_bridge_thickness], 0.7);
        }
        saddle_tunnel_cut();
    }
}

module previews() {
    if (show_previews) {
        %color([0, 0.8, 1, 0.35])
            translate([-zip_tie_band_width / 2, -zip_tie_bridge_length_along_y / 2 - 1.3, 0.25])
                cube([zip_tie_band_width, zip_tie_bridge_length_along_y + 2.6, zip_tie_band_thickness]);
        %color([1, 0.35, 0, 0.3])
            translate([0, 0, zip_tie_bridge_top_height + 2])
                rotate([0, 90, 0])
                    cylinder(h = saddle_total_width() + 3, d = 4, center = true);
    }
}

serviceable_cable_tie_saddle();
previews();
