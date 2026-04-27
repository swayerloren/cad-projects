// Pattern: phone stand side rail with screw tabs and triangular truss ribs.

$fn = 40;

module screw_tab(x, y, h = 4, d = 14, hole = 3.2) {
    difference() {
        translate([x, y, 0])
            cylinder(h = h, d = d);
        translate([x, y, -0.1])
            cylinder(h = h + 0.2, d = hole);
    }
}

module tube_between_points(p1, p2, r = 1) {
    v = [p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]];
    l = sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2]);
    axis = [-v[1], v[0], 0];
    angle = acos(v[2] / l);
    translate(p1)
        rotate(a = angle, v = axis)
            cylinder(h = l, r = r);
}

module trussed_side_rail(side = 1) {
    x = side * 36;
    screw_tab(x, -55);
    screw_tab(x, 65);

    for (i = [0 : 3]) {
        y0 = -42 + i * 24;
        y1 = y0 + 22;
        tube_between_points([x, y0, 4], [side * 26, (y0 + y1) / 2, 14], 1.2);
        tube_between_points([side * 26, (y0 + y1) / 2, 14], [x, y1, 4], 1.2);
    }
}

trussed_side_rail(-1);
trussed_side_rail(1);
