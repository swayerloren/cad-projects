// Heat-set insert boss with base pad and ribs.

$fn = 48;

boss_height = 6;
boss_outer_diameter = 8;
insert_hole_diameter = 4.2;
insert_depth = 5;
base_diameter = 15;
base_height = 2;
rib_length = 8;
rib_width = 2.4;
rib_height = 4;

module tapered_rib(angle) {
    rotate([0, 0, angle])
        hull() {
            translate([boss_outer_diameter / 2 - 0.2, -rib_width / 2, 0])
                cube([0.6, rib_width, rib_height]);
            translate([boss_outer_diameter / 2 + rib_length, -rib_width / 2, 0])
                cube([0.6, rib_width, 0.8]);
        }
}

module insert_boss() {
    difference() {
        union() {
            cylinder(h = base_height, d = base_diameter);
            cylinder(h = boss_height, d = boss_outer_diameter);
            for (a = [0, 90, 180, 270])
                tapered_rib(a);
        }
        translate([0, 0, boss_height - insert_depth - 0.02])
            cylinder(h = insert_depth + 0.05, d = insert_hole_diameter);
    }
}

insert_boss();
