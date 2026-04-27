// Pattern: local inside relief for a grommet/cable-gland collar.

wall_thickness = 3.5;
floor_thickness = 4.0;
wall_height = 20.0;

grommet_hole_diameter = 16;
grommet_inner_flange_diameter = 24;
grommet_clearance_margin = 2;
inside_grommet_clearance_diameter =
    grommet_inner_flange_diameter + 2 * grommet_clearance_margin;
inside_grommet_clearance_depth = 5;

grommet_center_x = 45;
grommet_center_z = floor_thickness + wall_height / 2;

module main_grommet_hole_cut() {
    translate([grommet_center_x, wall_thickness / 2, grommet_center_z])
        rotate([90, 0, 0])
            cylinder(h = wall_thickness + 4, d = grommet_hole_diameter, center = true);
}

module inside_grommet_collar_relief() {
    // Starts at inside wall face and cuts inward only.
    intersection() {
        translate([
            grommet_center_x,
            wall_thickness + inside_grommet_clearance_depth / 2,
            grommet_center_z
        ])
            rotate([90, 0, 0])
                cylinder(
                    h = inside_grommet_clearance_depth,
                    d = inside_grommet_clearance_diameter,
                    center = true
                );

        translate([
            grommet_center_x - inside_grommet_clearance_diameter / 2,
            wall_thickness,
            floor_thickness
        ])
            cube([
                inside_grommet_clearance_diameter,
                inside_grommet_clearance_depth,
                wall_height
            ]);
    }
}

module production_cutouts() {
    main_grommet_hole_cut();
    inside_grommet_collar_relief();
}
