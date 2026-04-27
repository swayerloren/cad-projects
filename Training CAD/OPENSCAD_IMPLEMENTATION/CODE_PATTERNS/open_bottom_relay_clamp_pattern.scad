// Open-bottom relay clamp pattern.
// Two screw feet plus a top bridge; no bottom tray under the relay.

$fn = 48;

relay_clamp_foot_width = 8;
relay_clamp_foot_length = 9;
relay_clamp_foot_thickness = 3;
relay_clamp_screw_spacing = 22;
relay_clamp_screw_diameter = 3.4;
relay_clamp_head_diameter = 6.5;
relay_clamp_head_recess_depth = 1.2;

relay_clamp_bridge_width = 10;
relay_clamp_bridge_length = relay_clamp_screw_spacing - relay_clamp_foot_length + 2;
relay_clamp_bridge_height = 14;
relay_clamp_bridge_thickness = 3;
relay_capture_lip_depth = 2;
relay_capture_lip_height = 2.5;

module rounded_rect_2d(w, d, r) {
    hull()
        for (x = [-w / 2 + r, w / 2 - r])
            for (y = [-d / 2 + r, d / 2 - r])
                translate([x, y])
                    circle(r = r);
}

module screw_foot(y) {
    translate([0, y, 0])
        linear_extrude(height = relay_clamp_foot_thickness)
            rounded_rect_2d(relay_clamp_foot_width, relay_clamp_foot_length, 1.5);
}

module open_bottom_relay_clamp() {
    difference() {
        union() {
            for (sy = [-1, 1])
                screw_foot(sy * relay_clamp_screw_spacing / 2);

            for (sy = [-1, 1])
                translate([
                    -relay_clamp_bridge_width / 2,
                    sy * (relay_clamp_screw_spacing / 2 - relay_clamp_foot_length / 2)
                        - relay_clamp_bridge_thickness / 2,
                    relay_clamp_foot_thickness
                ])
                    cube([
                        relay_clamp_bridge_width,
                        relay_clamp_bridge_thickness,
                        relay_clamp_bridge_height
                    ]);

            translate([
                -relay_clamp_bridge_width / 2,
                -relay_clamp_bridge_length / 2,
                relay_clamp_foot_thickness + relay_clamp_bridge_height
                    - relay_clamp_bridge_thickness
            ])
                cube([
                    relay_clamp_bridge_width,
                    relay_clamp_bridge_length,
                    relay_clamp_bridge_thickness
                ]);

            translate([
                -relay_clamp_bridge_width / 2,
                -relay_capture_lip_depth / 2,
                relay_clamp_foot_thickness + relay_clamp_bridge_height
                    - relay_clamp_bridge_thickness
                    - relay_capture_lip_height
                    + 0.05
            ])
                cube([
                    relay_clamp_bridge_width,
                    relay_capture_lip_depth,
                    relay_capture_lip_height
                ]);
        }

        for (sy = [-1, 1]) {
            y = sy * relay_clamp_screw_spacing / 2;
            translate([0, y, -0.05])
                cylinder(
                    h = relay_clamp_foot_thickness + 0.1,
                    d = relay_clamp_screw_diameter
                );
            translate([0, y, relay_clamp_foot_thickness - relay_clamp_head_recess_depth])
                cylinder(
                    h = relay_clamp_head_recess_depth + 0.1,
                    d = relay_clamp_head_diameter
                );
        }
    }
}

open_bottom_relay_clamp();
