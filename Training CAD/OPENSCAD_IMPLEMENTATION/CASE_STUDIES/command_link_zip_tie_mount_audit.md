# COMMAND LINK Zip-Tie Mount Audit

## Bad Pattern

A wall-integrated zip-tie bridge that only looks correct in a render is not enough. The design can still fail if:

- the bridge count is wrong
- slots are too small for a real tie
- slot mouths are sharp
- the PCB blocks access from above
- wire bundle clearance is not checked
- preview helpers leak into production STL
- slots accidentally cut through the exterior wall

## Good Pattern

Audit the feature as a serviceable mechanism:

- count left and right bridge features
- compare slot width and height to the selected zip tie
- preview the tie band through the upper/lower slots
- preview the wire bundle in the side lane
- preview the PCB at installed height
- verify standoff and solder-zone clearances
- keep cut depth inside the inward pad
- export production STL with preview helpers disabled

## COMMAND LINK Result

For the rugged lower enclosure:

- left long wall: 6 bridge features
- right long wall: 6 bridge features
- total: 12 bridge features
- slot size: 7.0 mm wide by 2.4 mm high
- nominal zip tie preview: 4.0 mm wide by 1.4 mm thick
- side lane: 2.5 mm PCB clearance, 6.0 mm wire lane, 0.4 mm lane-to-pad clearance
- exterior wall remains solid behind the slots

## OpenSCAD Notes

Use a mode split:

```scad
mode = "preview";
is_preview = mode == "preview";
is_production = mode == "production";

module main() {
    production_geometry();
    if (is_preview)
        preview_helpers();
}
```

Use named cutter helpers so later audits can distinguish real cutouts from visual previews:

```scad
module rounded_slot_cut(depth, width_y, height_z, radius, x0, zc) {
    rounded_yz_cut(depth, width_y, height_z, radius, x0, zc);
}

module chamfered_slot_cut(depth, width_y, height_z, chamfer, x0, zc) {
    rounded_yz_cut(
        depth,
        width_y + 2 * chamfer,
        height_z + 2 * chamfer,
        chamfer,
        x0,
        zc
    );
}
```

The preview should prove serviceability. The production STL should contain only the printable enclosure.
