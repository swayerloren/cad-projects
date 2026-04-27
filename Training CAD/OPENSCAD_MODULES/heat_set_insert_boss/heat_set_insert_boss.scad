// Reusable heat-set insert boss with base pad and optional gussets.

$fn = 36;

insert_hole_diameter = 4.2;
insert_depth = 5.0;
boss_outer_diameter = 8.0;
boss_height = 7.0;
base_diameter = 14.0;
base_height = 2.0;
gusset_enabled = true;
gusset_length = 8.0;
gusset_thickness = 2.0;
show_example = true;

module heat_set_insert_boss() {
    difference() {
        union() {
            cylinder(h = base_height, d = base_diameter);
            cylinder(h = boss_height, d = boss_outer_diameter);

            if (gusset_enabled) {
                for (a = [0, 90, 180, 270]) {
                    rotate([0, 0, a])
                        hull() {
                            translate([boss_outer_diameter / 2 - 0.2, -gusset_thickness / 2, 0])
                                cube([0.6, gusset_thickness, boss_height * 0.75]);
                            translate([gusset_length, -gusset_thickness / 2, 0])
                                cube([0.6, gusset_thickness, base_height]);
                        }
                }
            }
        }

        translate([0, 0, boss_height - insert_depth])
            cylinder(h = insert_depth + 0.1, d = insert_hole_diameter);
    }
}

if (show_example)
    heat_set_insert_boss();

