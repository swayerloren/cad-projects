# COMMAND LINK Grommet Entry

## What Failed

A long rectangular side opening was rejected because it looked like a random wall gap and was poor for dust/water resistance.

## Better Direction

Use one circular grommet or cable-gland hole on a short side of the enclosure.

Benefits:

- One intentional wire entry.
- Easier sealing with known hardware.
- Cleaner cable routing.
- Easier reinforcement with a boss/ring.

## OpenSCAD Difference Logic

The circular hole should be a cut cylinder that passes fully through the wall and boss:

```scad
module grommet_cut() {
    translate([center_x, wall_y, center_z])
        rotate([90, 0, 0])
            cylinder(h = wall_thickness + 2 * boss_projection + 2,
                     d = grommet_hole_diameter,
                     center = true);
}
```

Use it in the main assembly:

```scad
difference() {
    union() {
        wall_body();
        grommet_boss();
    }
    grommet_cut();
}
```

## Boss / Ring Reinforcement

The boss should be a separate solid module:

```scad
module grommet_boss() {
    translate([center_x, wall_face_y, center_z])
        rotate([90, 0, 0])
            cylinder(h = boss_projection, d = boss_outer_diameter);
}
```

## Rule

Exterior openings must be intentional, parameterized, and reinforced. A random wall gap is not a grommet feature.
