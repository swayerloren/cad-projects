# Sealed Lid With O-Ring Groove

Use a lid sealing interface as a system, not a cosmetic line.

A practical first-pass printed lid can include:

- top panel thick enough to resist screw clamp flex
- downward locating/sealing lip
- continuous O-ring groove around the perimeter
- screw holes planned around or outside the seal path
- preview O-ring helper
- base-side sealing ledge documented separately

Typical starting parameters:

```scad
oring_cross_section_diameter = 2.0;
oring_groove_width = 2.6;
oring_groove_depth = 1.4;
oring_compression_percent = 20;
lid_sealing_lip_depth = 3.0;
lid_sealing_lip_clearance = 0.35;
```

Validate the actual O-ring diameter, durometer, groove fill, compression, screw spacing, and clamp load with a printed test coupon before treating the enclosure as sealed.
