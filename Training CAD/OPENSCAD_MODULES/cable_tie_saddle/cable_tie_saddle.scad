// Reusable serviceable open-top cable-tie saddle.
// Design intent:
// - PCB or other hardware can already be installed.
// - The zip tie path remains visible and accessible from above.
// - The feature is internal-only and does not cut exterior walls.

$fn = 36;

zip_tie_band_width = 4.0;
zip_tie_band_thickness = 1.4;
zip_tie_tunnel_clear_width = 5.5;
zip_tie_tunnel_clear_height = 3.0;
zip_tie_bridge_thickness = 2.5;
zip_tie_bridge_top_height = 7.0;
zip_tie_bridge_span = 8.0;
zip_tie_bridge_length_along_y = 7.0;
zip_tie_foot_width = 2.8;
zip_tie_foot_length = 7.0;

wire_bundle_preview_diameter = 4.0;
show_zip_tie_path_preview = true;
show_wire_bundle_preview = true;

function saddle_total_width() = zip_tie_bridge_span + 2 * zip_tie_foot_width;

module rounded_rect_2d(w, d, r) {
    rr = max(0.01, min(r, min(w, d) / 2 - 0.01));
    hull() {
        for (x = [rr, w - rr])
            for (y = [rr, d - rr])
                translate([x, y])
                    circle(r = rr);
    }
}

module rounded_block(size, r = 1.0) {
    linear_extrude(height = size[2])
        rounded_rect_2d(size[0], size[1], r);
}

module cable_tie_saddle_tunnel_cut() {
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
                rounded_block([zip_tie_foot_width, foot_y, foot_h], 0.8);

            translate([total_x / 2 - zip_tie_foot_width, -foot_y / 2, 0])
                rounded_block([zip_tie_foot_width, foot_y, foot_h], 0.8);

            translate([
                -total_x / 2,
                -zip_tie_bridge_length_along_y / 2,
                bridge_bottom
            ])
                rounded_block([
                    total_x,
                    zip_tie_bridge_length_along_y,
                    zip_tie_bridge_thickness
                ], 0.8);
        }

        cable_tie_saddle_tunnel_cut();
    }
}

module zip_tie_path_preview() {
    if (show_zip_tie_path_preview)
        %color([0.1, 0.8, 1.0, 0.35])
            translate([
                -zip_tie_band_width / 2,
                -zip_tie_bridge_length_along_y / 2 - 1.3,
                0.25
            ])
                cube([
                    zip_tie_band_width,
                    zip_tie_bridge_length_along_y + 2.6,
                    zip_tie_band_thickness
                ]);
}

module wire_bundle_preview() {
    if (show_wire_bundle_preview)
        %color([1.0, 0.35, 0.05, 0.30])
            translate([
                0,
                0,
                zip_tie_bridge_top_height + wire_bundle_preview_diameter / 2
            ])
                rotate([0, 90, 0])
                    cylinder(
                        h = saddle_total_width() + 3.0,
                        d = wire_bundle_preview_diameter,
                        center = true
                    );
}

serviceable_cable_tie_saddle();
zip_tie_path_preview();
wire_bundle_preview();
