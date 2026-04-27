// Pattern: direct STL overlay while rebuilding a parametric part.
// Keep the original STL coordinate frame until the rebuild matches.

$fn = 48;

show_reference_stl = true;
show_rebuild = true;
reference_alpha = 0.30;

part_x0 = -20;
part_x1 = 20;
part_y0 = -10;
part_y1 = 10;
part_z0 = 0;
part_z1 = 6;

module box(x0, x1, y0, y1, z0, z1) {
    translate([x0, y0, z0])
        cube([x1 - x0, y1 - y0, z1 - z0], center=false);
}

module reference_stl() {
    color([1.0, 0.45, 0.15, reference_alpha])
        import("reference_part.stl", convexity=8);
}

module rebuilt_part() {
    difference() {
        box(part_x0, part_x1, part_y0, part_y1, part_z0, part_z1);
        translate([0, 0, part_z1 / 2])
            rotate([90, 0, 0])
                cylinder(h=part_y1 - part_y0 + 2, r=2, center=true);
    }
}

if (show_reference_stl)
    reference_stl();

if (show_rebuild)
    color([0.15, 0.40, 1.0, 0.65])
        rebuilt_part();
