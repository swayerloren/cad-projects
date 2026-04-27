// Relay bracket insert boss pattern for a removable lid.

$fn = 48;

relay_bracket_screw_spacing = 22;
relay_bracket_insert_hole_diameter = 4.2;
relay_bracket_insert_depth = 5.0;
relay_bracket_boss_od = 7.0;
relay_bracket_boss_height = 5.5;
relay_boss_rib_thickness = 2.0;
relay_boss_rib_height = 3.0;

module relay_mount_boss_pair(x = 0, y = 0) {
    difference() {
        union() {
            for (dy = [-relay_bracket_screw_spacing / 2, relay_bracket_screw_spacing / 2])
                translate([x, y + dy, -relay_bracket_boss_height])
                    cylinder(h = relay_bracket_boss_height + 0.05, d = relay_bracket_boss_od);

            translate([
                x - relay_boss_rib_thickness / 2,
                y - relay_bracket_screw_spacing / 2,
                -relay_boss_rib_height
            ])
                cube([
                    relay_boss_rib_thickness,
                    relay_bracket_screw_spacing,
                    relay_boss_rib_height + 0.05
                ]);
        }

        for (dy = [-relay_bracket_screw_spacing / 2, relay_bracket_screw_spacing / 2])
            translate([x, y + dy, -relay_bracket_boss_height - 0.05])
                cylinder(
                    h = relay_bracket_insert_depth,
                    d = relay_bracket_insert_hole_diameter
                );
    }
}

relay_mount_boss_pair();
