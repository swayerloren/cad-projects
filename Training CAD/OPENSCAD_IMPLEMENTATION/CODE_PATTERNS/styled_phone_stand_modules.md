# Pattern: Styled Phone Stand Modules

## Recommended Parameters

```scad
phone_width = 76;
phone_thickness = 12;
backrest_angle = 12;
slot_width = 44;
slot_depth = 13;
cable_cutout_size = [34, 19];
side_bolster_d = 7;
```

## Recommended Modules

```scad
module base() {}
module seat_pan() {}
module backrest() {}
module side_bolsters() {}
module phone_slot() {}
module cable_cutout() {}
module style_ribs() {}
module assembly_preview() {}
module main() {}
```

## Tube Frame Performance Pattern

Prefer vector-aligned cylinders for rollcages:

```scad
module tube_between(p1, p2, d) {
    v = p2 - p1;
    translate(p1)
        rotate(a = acos(v.z / norm(v)), v = cross([0,0,1], v))
            cylinder(d = d, h = norm(v));
}
```

This exports faster than hulling many spheres.
