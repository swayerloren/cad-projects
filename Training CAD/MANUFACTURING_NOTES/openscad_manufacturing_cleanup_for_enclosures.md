# OpenSCAD Manufacturing Cleanup For Enclosures

## Problem

OpenSCAD enclosure prototypes often start as functional but boxy geometry:

- abrupt boss cylinders
- square-ended gussets
- sharp internal slot mouths
- hard rectangular pads
- fragile-looking top rims
- large solid blocks instead of molded transitions

That can print, but it looks crude and creates stress risers. It is also a poor starting point for future injection molding.

## Good Cleanup Pattern

Improve only the manufacturing surfaces and transitions first:

- keep confirmed PCB holes and functional openings fixed
- add named edge/chamfer/blend parameters
- use rounded rectangle pads for low rectangular features
- use tapered cylinders under bosses
- seed gusset hulls with cylinders instead of square blocks
- soften slot mouths with rounded or oversized shallow cutters
- keep preview helpers out of production export
- document what remains FDM-only versus molding-ready

## OpenSCAD Guidance

Prefer fast, reliable approximations:

```scad
edge_chamfer = 0.8;
slot_edge_chamfer = 0.5;
boss_blend_radius = 1.5;

module boss_blend_pad(d_base, d_top, h) {
    cylinder(h = h, d1 = d_base, d2 = d_top);
}

module rounded_box_approx(size, r) {
    linear_extrude(height = size[2])
        rounded_box_2d(size[0], size[1], r);
}
```

Avoid repeated true fillets across many features if they make export unreliable. `minkowski()`, nested `hull()`, and `offset()` can be useful on one or two features, but they can make a production STL painfully slow on a whole enclosure.

## Injection Molding Awareness

For a future molded version, review:

- draft
- side holes that need side cores
- internal tunnels that need side actions
- cored bosses
- sink risk around thick bosses
- rib thickness versus wall thickness
- parting-line and ejector strategy

An FDM cleanup pass should not claim the part is injection-mold-ready. It should make the prototype cleaner while documenting the tooling work still required.
