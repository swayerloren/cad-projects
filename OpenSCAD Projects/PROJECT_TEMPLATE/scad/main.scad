// OpenSCAD project template.
// Use mode = "production" for STL export.

mode = "preview"; // "preview" or "production"
$fn = mode == "production" ? 64 : 32;

include <shared_dimensions.scad>

module production_geometry() {
    cube([40, 30, wall_thickness], center = true);
}

module preview_helpers() {
    color([0, 0.45, 1, 0.25])
        translate([0, 0, 8])
            cube([42, 32, 12], center = true);
}

module main() {
    production_geometry();

    if (mode == "preview") {
        preview_helpers();
    }
}

main();

