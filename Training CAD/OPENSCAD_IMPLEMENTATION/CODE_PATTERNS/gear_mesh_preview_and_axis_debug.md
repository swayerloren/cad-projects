# OpenSCAD Code Pattern: Gear Mesh Preview And Axis Debug

## Purpose

Use preview-only geometry to validate a gear train before judging the model by appearance.

## Pattern

Define gear parameters:

```scad
drive_teeth = 32;
drive_pitch_d = 64;
driven_teeth = 22;
driven_pitch_d = 44;
gear_module = 2;
```

Draw pitch circles:

```scad
module thin_disc(d, h = 0.4, wall = 0.6) {
    difference() {
        cylinder(d = d + wall, h = h);
        translate([0, 0, -0.02])
            cylinder(d = d - wall, h = h + 0.04);
    }
}
```

Draw axis lines:

```scad
module axis_line(center, z0, z1, d = 1.2) {
    translate([center[0], center[1], z0])
        cylinder(d = d, h = z1 - z0);
}
```

Draw center-distance bars:

```scad
module debug_bar(p1, p2, z, d = 1) {
    hull() {
        translate([p1[0], p1[1], z]) sphere(d = d);
        translate([p2[0], p2[1], z]) sphere(d = d);
    }
}
```

## Review Checklist

- Do pitch circles touch at each intended mesh?
- Are shared-shaft gears exactly coaxial?
- Are lower and upper gear planes separated correctly?
- Do plates, collars, and stops leave rotation clearance?
- Is the cable, tape, belt, or material path visible?

## Caution

Pitch debug geometry must stay preview-only. Do not merge it into printable part modules.

