// Trussed side rail base pattern.
// Useful when a styled base should not become a plain rectangle.

$fn = 36;

rail_length = 135;
rail_width = 10.5;
rail_spacing = 64;
rail_thickness = 2.2;
hole_d = 3.2;
boss_d = 12;
web_w = 3.2;

module capsule_between_2d(p1, p2, d) {
    hull() {
        translate(p1) circle(d = d);
        translate(p2) circle(d = d);
    }
}

module side_rail(side = -1) {
    x = side * rail_spacing / 2;

    linear_extrude(height = rail_thickness)
        capsule_between_2d([x, -rail_length / 2 + rail_width / 2],
                           [x,  rail_length / 2 - rail_width / 2],
                           rail_width);

    for (y = [-58, 58, -16, 32])
        translate([x, y, rail_thickness])
            cylinder(d = boss_d, h = 0.8);
}

module truss_web() {
    linear_extrude(height = rail_thickness + 0.4)
        for (y = [-44, -10, 24]) {
            capsule_between_2d([-rail_spacing / 2, y - 15],
                               [ rail_spacing / 2, y + 15],
                               web_w);
            capsule_between_2d([ rail_spacing / 2, y - 15],
                               [-rail_spacing / 2, y + 15],
                               web_w);
        }
}

module rail_holes() {
    for (sx = [-1, 1])
        for (y = [-58, 58, -16, 32])
            translate([sx * rail_spacing / 2, y, -0.02])
                cylinder(d = hole_d, h = rail_thickness + 2);
}

difference() {
    union() {
        side_rail(-1);
        side_rail(1);
        truss_web();
    }
    rail_holes();
}
