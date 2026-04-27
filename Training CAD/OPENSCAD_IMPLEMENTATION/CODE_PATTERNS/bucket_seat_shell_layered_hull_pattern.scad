// Pattern: bucket seat shell from layered hull profiles.
// Use this for styled seats where exact organic surfaces are not available.

$fn = 48;

module rounded_rect_2d(w, h, r) {
    rr = min(r, min(w, h) / 2 - 0.01);
    hull() {
        for (x = [-w / 2 + rr, w / 2 - rr])
            for (y = [-h / 2 + rr, h / 2 - rr])
                translate([x, y])
                    circle(r = rr);
    }
}

module layer(width, thick, z, h = 8, r = 4) {
    translate([0, 0, z])
        linear_extrude(height = h, center = true)
            rounded_rect_2d(width, thick, r);
}

module bucket_back_shell() {
    hull() {
        layer(46, 8, 8);
        layer(36, 8, 40);
        layer(64, 9, 76);
        layer(48, 9, 102);
    }
}

bucket_back_shell();
