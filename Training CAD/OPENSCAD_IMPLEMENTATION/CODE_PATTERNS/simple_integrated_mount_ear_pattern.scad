// Simple integrated external mounting ear pattern.
// Use as a starting point, then adapt coordinate mapping to the enclosure.

$fn = 48;

mount_ear_length = 18;
mount_ear_width = 16;
mount_ear_thickness = 5;
mount_hole_diameter = 4.3;
mount_boss_outer_diameter = 10;
mount_boss_height = 1.5;
mount_boss_chamfer = 0.8;
mount_neck_width = 16;
mount_neck_blend_radius = 3;
mount_gusset_thickness = 3;
mount_gusset_height = 7;
mount_gusset_length = 10;
mount_edge_chamfer = 0.8;

module mount_ear_body_footprint_2d(hole_x, root_x, y = 0, shrink = 0) {
    root_r = min(mount_neck_blend_radius, mount_neck_width / 2 - 0.1);
    lug_r = mount_ear_width / 2;

    offset(delta = -shrink)
        hull() {
            translate([hole_x, y])
                circle(r = lug_r);
            translate([root_x, y - mount_neck_width / 2 + root_r])
                circle(r = root_r);
            translate([root_x, y + mount_neck_width / 2 - root_r])
                circle(r = root_r);
        }
}

module simple_mount_ear(hole_x = -9, root_x = 3.5, y = 0) {
    difference() {
        union() {
            linear_extrude(height = mount_ear_thickness - mount_edge_chamfer)
                mount_ear_body_footprint_2d(hole_x, root_x, y, 0);

            translate([0, 0, mount_ear_thickness - mount_edge_chamfer - 0.01])
                linear_extrude(height = mount_edge_chamfer + 0.01)
                    mount_ear_body_footprint_2d(
                        hole_x,
                        root_x,
                        y,
                        mount_edge_chamfer * 0.45
                    );

            translate([hole_x, y, mount_ear_thickness - 0.01])
                cylinder(
                    h = mount_boss_height + 0.01,
                    d1 = mount_boss_outer_diameter,
                    d2 = mount_boss_outer_diameter - 2 * mount_boss_chamfer
                );
        }

        translate([hole_x, y, -0.5])
            cylinder(
                h = mount_ear_thickness + mount_boss_height + 1,
                d = mount_hole_diameter
            );
    }
}

simple_mount_ear();
