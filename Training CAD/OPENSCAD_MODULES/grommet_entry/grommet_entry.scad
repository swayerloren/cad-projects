// Reusable circular grommet or cable-gland entry in a wall.

$fn = 48;

wall_width = 42.0;
wall_height = 28.0;
wall_thickness = 3.5;
hole_diameter = 16.0;
boss_outer_diameter = 24.0;
boss_thickness = 3.0;
show_example = true;

module grommet_entry_wall() {
    difference() {
        union() {
            translate([-wall_width / 2, 0, 0])
                cube([wall_width, wall_thickness, wall_height]);

            translate([0, -boss_thickness, wall_height / 2])
                rotate([90, 0, 0])
                    cylinder(h = boss_thickness, d = boss_outer_diameter);
        }

        translate([0, wall_thickness / 2, wall_height / 2])
            rotate([90, 0, 0])
                cylinder(h = wall_thickness + 2 * boss_thickness + 1, d = hole_diameter, center = true);
    }
}

if (show_example)
    grommet_entry_wall();

