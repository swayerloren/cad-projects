// Reusable tube-between-points pattern for roll cages, braces, and frames.

$fn = 36;

function vsub(a, b) = [a[0] - b[0], a[1] - b[1], a[2] - b[2]];
function vlen(v) = sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2]);
function vcross(a, b) = [
    a[1] * b[2] - a[2] * b[1],
    a[2] * b[0] - a[0] * b[2],
    a[0] * b[1] - a[1] * b[0]
];

module tube_between_points(p1, p2, radius = 1.5) {
    v = vsub(p2, p1);
    l = vlen(v);
    axis = vcross([0, 0, 1], v);
    axis_len = vlen(axis);
    angle = l == 0 ? 0 : acos(v[2] / l);

    if (l > 0.01)
        translate(p1)
            rotate(a = angle, v = axis_len < 0.01 ? [1, 0, 0] : axis)
                cylinder(r = radius, h = l);
}

// Example
tube_between_points([0, 0, 0], [30, 10, 40], 1.75);
