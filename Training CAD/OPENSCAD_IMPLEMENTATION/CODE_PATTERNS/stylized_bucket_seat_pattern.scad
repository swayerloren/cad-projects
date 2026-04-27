// Stylized bucket seat pattern for OpenSCAD.
// Uses a profile shell, real openings, side bolsters, and a front phone lip.

$fn = 40;

module rounded_rect_2d(size, r) {
    hull()
        for (x = [-size[0] / 2 + r, size[0] / 2 - r])
            for (y = [-size[1] / 2 + r, size[1] / 2 - r])
                translate([x, y])
                    circle(r = r);
}

module xz_plate(thick_y) {
    rotate([90, 0, 0])
        linear_extrude(height = thick_y, center = true)
            children();
}

module backrest_profile_2d() {
    polygon([
        [-22, 0], [-20, 30], [-31, 62], [-21, 94],
        [21, 94], [31, 62], [20, 30], [22, 0]
    ]);
}

module harness_openings(thick = 7) {
    for (sx = [-1, 1])
        translate([sx * 13, 0, 76])
            rotate([0, 0, sx * 18])
                xz_plate(thick)
                    rounded_rect_2d([17, 5], 2.3);

    translate([0, 0, 30])
        xz_plate(thick)
            rounded_rect_2d([21, 8], 3.5);
}

module front_phone_lip(width = 56, height = 10) {
    translate([0, -32, height / 2])
        rotate([0, 90, 0])
            cylinder(d = height, h = width, center = true);
}

module stylized_bucket_seat() {
    difference() {
        xz_plate(5)
            backrest_profile_2d();
        harness_openings(7);
    }

    color("black")
        translate([0, -3, 42])
            xz_plate(1.2)
                rounded_rect_2d([34, 58], 4);

    front_phone_lip();
}

stylized_bucket_seat();
