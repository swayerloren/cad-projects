# Boolean Operations

OpenSCAD parts are built with constructive solid geometry. Correct boolean structure is what separates real holes and tunnels from fake visual notches.

## `union()`

Use `union()` to combine solids.

```scad
module part_body() {
    union() {
        cube([40, 20, 4]);
        translate([10, 10, 4]) cylinder(h = 8, d = 10);
    }
}
```

## `difference()`

Use `difference()` to subtract holes, slots, tunnels, and reliefs.

```scad
module hole_cut() {
    translate([10, 10, -0.5])
        cylinder(h = 10, d = 4);
}

difference() {
    part_body();
    hole_cut();
}
```

The cut should extend through the target with small overlap. A cut that ends exactly at a face can leave artifacts.

## `intersection()`

Use `intersection()` to keep only overlapping regions, often for trimmed shapes or controlled cutaways.

## `hull()`

Use `hull()` for simple rounded or blended forms, such as mount ears and transition pads.

```scad
hull() {
    translate([0, 0]) circle(d = 12);
    translate([20, 0]) circle(d = 8);
}
```

## `minkowski()`

Use `minkowski()` carefully. It can create nice rounded forms but may render slowly and can inflate dimensions if not planned.

## Cutout Rules

- Cut geometry must actually intersect the solid.
- Cut geometry should be slightly longer than the target.
- Use epsilon overlap such as `-0.05` and `+0.1`.
- Keep cut modules separate from feature body modules.
- Name cut modules clearly: `grommet_cut()`, `screw_hole_cut()`, `tie_tunnel_cut()`.

## Common Mistakes

- Subtracting a cutout that does not reach the solid.
- Cutout too short to pass through.
- Cutout flush with a face, causing z-fighting or artifacts.
- Creating a fake visual slot by adding dark geometry instead of subtracting.
- Forgetting tolerance around real hardware.
- Accidentally cutting through exterior walls with internal strain-relief slots.

## Pattern

```scad
module feature_body() { ... }
module feature_cut() { ... }

module finished_feature() {
    difference() {
        feature_body();
        feature_cut();
    }
}
```
