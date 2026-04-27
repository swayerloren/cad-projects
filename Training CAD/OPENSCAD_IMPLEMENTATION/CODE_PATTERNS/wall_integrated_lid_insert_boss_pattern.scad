// Wall-integrated lid insert boss pattern.
// The boss center is pulled close to the inside wall, then a full-height web
// merges the round insert boss into the side-wall service spine.

wall_thickness = 3.5;
wall_lid_boss_od = 8.0;
wall_lid_boss_insert_hole_diameter = 4.2;
wall_lid_boss_insert_depth = 5.0;
wall_lid_boss_z0 = 4.0;
wall_lid_boss_height = 21.7;

module wall_lid_boss_reinforcement(p, body_width) {
    side = (p[0] < body_width / 2) ? -1 : 1;
    r = wall_lid_boss_od / 2;
    web_y = wall_lid_boss_od + 1.2;

    if (side < 0)
        translate([wall_thickness - 0.04, p[1] - web_y / 2, wall_lid_boss_z0])
            cube([p[0] - wall_thickness + r + 0.04, web_y, wall_lid_boss_height]);
    else
        translate([p[0] - r, p[1] - web_y / 2, wall_lid_boss_z0])
            cube([body_width - wall_thickness - (p[0] - r) + 0.04, web_y, wall_lid_boss_height]);
}

module wall_integrated_lid_insert_boss(p, body_width) {
    wall_lid_boss_reinforcement(p, body_width);
    translate([p[0], p[1], wall_lid_boss_z0])
        cylinder(h = wall_lid_boss_height, d = wall_lid_boss_od);
}

module wall_lid_boss_hole_cut(p, top_z) {
    translate([p[0], p[1], top_z - wall_lid_boss_insert_depth])
        cylinder(
            h = wall_lid_boss_insert_depth + 0.1,
            d = wall_lid_boss_insert_hole_diameter
        );
}
