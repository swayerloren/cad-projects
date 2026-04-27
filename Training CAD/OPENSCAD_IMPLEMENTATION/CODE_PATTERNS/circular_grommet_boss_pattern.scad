// Circular grommet/cable gland hole through a wall with reinforcing boss.

$fn = 64;

wall_width = 50;
wall_thickness = 4;
wall_height = 30;
hole_diameter = 16;
boss_outer_diameter = 24;
boss_projection = 3;
hole_center_z = wall_height / 2;

module wall_body() {
    cube([wall_width, wall_thickness, wall_height]);
}

module grommet_boss() {
    translate([wall_width / 2, 0, hole_center_z])
        rotate([90, 0, 0])
            cylinder(h = boss_projection, d = boss_outer_diameter);
}

module grommet_cut() {
    translate([wall_width / 2, wall_thickness / 2, hole_center_z])
        rotate([90, 0, 0])
            cylinder(h = wall_thickness + 2 * boss_projection + 2, d = hole_diameter, center = true);
}

difference() {
    union() {
        wall_body();
        grommet_boss();
    }
    grommet_cut();
}
