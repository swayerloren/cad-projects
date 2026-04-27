# Printed Shaft and Standoff Design Notes

## Observed Pattern

The cable wrapping machine uses printed posts and standoffs instead of metal fasteners:

- lower plate has D14 standoff bodies
- upper plate has about D12.3 post holes
- rotating parts use about D13-D14 bore/post relationships
- tape roller uses about D14.5 bore around a D14 post

## Design Guidance

- Use larger printed shaft diameters than metal pins because layer adhesion and wear are limiting factors.
- Add washers or sacrificial collars where rotating parts rub against plates.
- Make fixed standoffs serviceable with screws or heat-set inserts when repair matters.
- Keep rotating posts short when possible to reduce bending.
- Document whether a post is fixed, glued, or rotating; the same cylinder can mean very different things mechanically.

## OpenSCAD Parameters To Expose

```scad
shaft_d = 14;
shaft_clearance = 0.3;
standoff_d = 14;
standoff_tip_d = 12;
plate_hole_d = standoff_tip_d + shaft_clearance;
washer_d = 30;
washer_h = 5;
```
