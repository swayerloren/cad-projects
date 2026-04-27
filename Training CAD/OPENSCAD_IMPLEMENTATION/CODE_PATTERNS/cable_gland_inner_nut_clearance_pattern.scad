// Cable gland inner nut clearance pattern.
// Uses a real production relief cut plus preview-only hardware.

$fn = 64;

wall_thickness = 3.5;
wall_height = 20;
floor_thickness = 4;

hole_d = 16;
nut_d = 28;
nut_thickness = 5;
tool_clearance_d = 34;
relief_depth = 8;
relief_width = tool_clearance_d + 4;
center_x = 40;
center_z = floor_thickness + wall_height / 2;

show_preview = true;

module gland_hole_cut() {
    translate([center_x, wall_thickness / 2, center_z])
        rotate([90, 0, 0])
            cylinder(h = wall_thickness + 4, d = hole_d, center = true);
}

module inner_nut_relief_cut() {
    translate([
        center_x - relief_width / 2,
        wall_thickness - 0.05,
        0
    ])
        cube([
            relief_width,
            relief_depth + 0.1,
            floor_thickness + wall_height - 0.05
        ]);
}

module wall_with_gland_relief() {
    difference() {
        cube([80, wall_thickness, floor_thickness + wall_height]);
        gland_hole_cut();
        inner_nut_relief_cut();
    }
}

module preview_gland_hardware() {
    if (show_preview) {
        %color([1, 0.65, 0, 0.35])
            translate([center_x, wall_thickness, center_z])
                rotate([-90, 0, 0])
                    cylinder(h = nut_thickness, d = nut_d, $fn = 6);

        %color([1, 0, 0, 0.15])
            translate([center_x, wall_thickness, center_z])
                rotate([-90, 0, 0])
                    cylinder(h = relief_depth, d = tool_clearance_d);
    }
}

wall_with_gland_relief();
preview_gland_hardware();
