// Reusable refined rounded external mounting ear.
// The ear is modeled as an oval/teardrop lug with a broad root neck,
// raised screw boss, and two clean gussets.

$fn = 40;

ear_length = 20.0;
ear_width = 14.0;
ear_thickness = 5.0;
ear_radius = 5.0;
hole_diameter = 4.2;
boss_outer_diameter = 11.0;
boss_height = 2.5;
neck_width = 12.0;
neck_overlap = 4.0;
edge_rounding = 2.0;
gusset_thickness = 2.5;
gusset_height = 6.0;
gusset_length = 10.0;
show_example_body_stub = true;

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

module mount_ear_boss(x, y, thickness, boss_d, boss_h) {
    translate([x, y, thickness])
        cylinder(h = boss_h, d = boss_d);
}

module mount_ear_gusset(x0, y0, x1, y1, thickness, height) {
    hull() {
        translate([x0 - thickness / 2, y0 - thickness / 2, ear_thickness])
            cube([thickness, thickness, height]);
        translate([x1 - thickness / 2, y1 - thickness / 2, ear_thickness])
            cube([thickness, thickness, 0.8]);
    }
}

module refined_mount_ear(
    length = ear_length,
    width = ear_width,
    thickness = ear_thickness,
    hole_d = hole_diameter,
    boss_d = boss_outer_diameter,
    boss_h = boss_height
) {
    screw_x = length / 2;
    root_x = 0;
    root_r = min(edge_rounding, neck_width / 2 - 0.1);
    rib_y = neck_width / 2 - gusset_thickness / 2;

    difference() {
        union() {
            linear_extrude(height = thickness)
                union() {
                    hull() {
                        translate([screw_x, 0])
                            circle(d = width);
                        translate([root_x, -neck_width / 2 + root_r])
                            circle(r = root_r);
                        translate([root_x, neck_width / 2 - root_r])
                            circle(r = root_r);
                    }

                    translate([-neck_overlap, -neck_width / 2])
                        rounded_rect_2d(
                            neck_overlap + length * 0.42,
                            neck_width,
                            edge_rounding
                        );
                }

            mount_ear_boss(screw_x, 0, thickness, boss_d, boss_h);

            mount_ear_gusset(
                root_x + edge_rounding,
                -rib_y,
                screw_x - gusset_length * 0.55,
                -rib_y,
                gusset_thickness,
                gusset_height
            );
            mount_ear_gusset(
                root_x + edge_rounding,
                rib_y,
                screw_x - gusset_length * 0.55,
                rib_y,
                gusset_thickness,
                gusset_height
            );
        }

        translate([screw_x, 0, -0.5])
            cylinder(h = thickness + boss_h + 1.0, d = hole_d);
    }
}

if (show_example_body_stub) {
    translate([-8, -12, 0])
        rounded_block([8, 24, ear_thickness + gusset_height], 2.0);
}

refined_mount_ear();
