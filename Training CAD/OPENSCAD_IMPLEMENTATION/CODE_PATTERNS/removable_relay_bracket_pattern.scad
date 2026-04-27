// Pattern: removable two-screw relay retainer strap.

$fn = 48;

relay_bracket_screw_spacing = 22;
relay_bracket_screw_clearance_diameter = 3.4;
relay_bracket_screw_head_clearance_diameter = 6.5;
relay_bracket_screw_head_recess_depth = 1.2;

base_thickness = 3;
bridge_height = 14;
wall_thickness = 2.5;
foot_width = 18;
foot_depth = 8.5;
bridge_width = 8;
bridge_length = relay_bracket_screw_spacing - foot_depth + 2;
capture_lip_height = 2.5;
capture_lip_depth = 2;

module rounded_box_2d(w, d, r) {
    rr = min(r, min(w, d) / 2 - 0.01);
    hull()
        for (x = [rr, w - rr])
            for (y = [rr, d - rr])
                translate([x, y])
                    circle(r = rr);
}

module centered_rounded_block(size, r = 1) {
    linear_extrude(height = size[2])
        translate([-size[0] / 2, -size[1] / 2])
            rounded_box_2d(size[0], size[1], r);
}

module relay_retainer_bracket() {
    difference() {
        union() {
            for (sy = [-1, 1])
                translate([0, sy * relay_bracket_screw_spacing / 2, 0])
                    centered_rounded_block([foot_width, foot_depth, base_thickness], 2);

            for (sy = [-1, 1])
                translate([
                    -bridge_width / 2,
                    sy * (relay_bracket_screw_spacing / 2 - foot_depth / 2)
                        - wall_thickness / 2,
                    base_thickness
                ])
                    cube([bridge_width, wall_thickness, bridge_height]);

            translate([
                -bridge_width / 2,
                -bridge_length / 2,
                base_thickness + bridge_height - wall_thickness
            ])
                cube([bridge_width, bridge_length, wall_thickness]);

            translate([
                -bridge_width / 2,
                -capture_lip_depth / 2,
                base_thickness + bridge_height - wall_thickness - capture_lip_height
            ])
                cube([bridge_width, capture_lip_depth, capture_lip_height]);
        }

        for (sy = [-1, 1]) {
            translate([0, sy * relay_bracket_screw_spacing / 2, -0.05])
                cylinder(h = base_thickness + bridge_height + 1, d = relay_bracket_screw_clearance_diameter);

            translate([
                0,
                sy * relay_bracket_screw_spacing / 2,
                base_thickness - relay_bracket_screw_head_recess_depth
            ])
                cylinder(h = relay_bracket_screw_head_recess_depth + 0.1, d = relay_bracket_screw_head_clearance_diameter);
        }
    }
}

relay_retainer_bracket();
