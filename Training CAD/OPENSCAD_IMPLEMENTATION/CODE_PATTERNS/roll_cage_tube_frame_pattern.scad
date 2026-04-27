// Pattern: roll cage / tube frame from cylinders between points.

$fn = 48;

function vsub(a, b) = [a[0] - b[0], a[1] - b[1], a[2] - b[2]];
function vlen(v) = sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2]);
function vcross(a, b) = [
    a[1] * b[2] - a[2] * b[1],
    a[2] * b[0] - a[0] * b[2],
    a[0] * b[1] - a[1] * b[0]
];

module tube_between_points(p1, p2, r = 1.5, joint_spheres = true) {
    v = vsub(p2, p1);
    l = vlen(v);
    if (l > 0.01) {
        axis = vcross([0, 0, 1], v);
        angle = acos(v[2] / l);
        translate(p1) {
            if (vlen(axis) < 0.001)
                cylinder(h = l, r = r);
            else
                rotate(a = angle, v = axis)
                    cylinder(h = l, r = r);
            if (joint_spheres)
                sphere(r = r);
        }
        if (joint_spheres)
            translate(p2)
                sphere(r = r);
    }
}

module simple_hoop() {
    tube_between_points([-30, 0, 0], [-24, 0, 70], 2);
    tube_between_points([-24, 0, 70], [-12, 0, 100], 2);
    tube_between_points([-12, 0, 100], [12, 0, 100], 2);
    tube_between_points([12, 0, 100], [24, 0, 70], 2);
    tube_between_points([24, 0, 70], [30, 0, 0], 2);
}

simple_hoop();
