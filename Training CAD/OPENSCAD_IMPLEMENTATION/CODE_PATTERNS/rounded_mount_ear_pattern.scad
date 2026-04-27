// Rounded external mount ear with boss, clearance hole, neck, and gusset.

$fn = 48;

ear_length = 22;
ear_width = 14;
ear_thickness = 5;
mount_hole_diameter = 4.2;
boss_outer_diameter = 11;
boss_height = 2.5;
neck_width = 12;
neck_length = 10;
gusset_thickness = 2.5;
gusset_height = 6;

module rounded_ear_2d() {
    hull() {
        translate([ear_length, 0]) circle(d = ear_width);
        translate([0, -neck_width / 2]) square([0.5, neck_width]);
    }
}

module ear_body() {
    linear_extrude(height = ear_thickness)
        union() {
            rounded_ear_2d();
            translate([-neck_length, -neck_width / 2])
                square([neck_length + 1, neck_width]);
        }
}

module boss() {
    translate([ear_length, 0, ear_thickness])
        cylinder(h = boss_height, d = boss_outer_diameter);
}

module hole_cut() {
    translate([ear_length, 0, -0.5])
        cylinder(h = ear_thickness + boss_height + 1.0, d = mount_hole_diameter);
}

module gusset(y) {
    hull() {
        translate([0, y - gusset_thickness / 2, ear_thickness])
            cube([gusset_thickness, gusset_thickness, gusset_height]);
        translate([ear_length * 0.65, y - gusset_thickness / 2, ear_thickness])
            cube([gusset_thickness, gusset_thickness, 0.8]);
    }
}

module rounded_mount_ear() {
    difference() {
        union() {
            ear_body();
            boss();
            gusset(-neck_width / 2 + gusset_thickness);
            gusset(neck_width / 2 - gusset_thickness);
        }
        hole_cut();
    }
}

rounded_mount_ear();
