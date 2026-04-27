# Coordinate Systems

Most enclosure mistakes come from unclear coordinate systems. Define the origin and mapping rules before modeling features.

## Common Coordinate Frames

### PCB Local Coordinates

PCB-local coordinates usually come from a PCB file, with `[0, 0]` at the board outline minimum corner.

For COMMAND LINK:

- X is board width, `0` to `65.000 mm`.
- Y is board length, `0` to `78.710 mm`.

### Enclosure Coordinates

The enclosure may use its own origin at the lower-left outside corner of the body.

### PCB Origin Inside Enclosure

The PCB is placed inside the enclosure by margins.

```scad
pcb_origin_x = carrier_margin_left;
pcb_origin_y = carrier_margin_front;
```

Use mapping helpers:

```scad
function pcb_x(x) = pcb_origin_x + x;
function pcb_y(y) = pcb_origin_y + y;
```

Then place source-derived PCB features like this:

```scad
translate([pcb_x(2.600), pcb_y(2.900), floor_thickness])
    pcb_standoff();
```

## Why This Matters

- Mounting holes map directly to standoffs.
- Wire pad zones map directly to wire channels and strain relief.
- Component keepouts map directly to lid and wall clearances.
- Future board revisions can be updated by changing source facts and margins.

## Avoid

- Manually adding offsets in every `translate()`.
- Mixing board-local coordinates and enclosure coordinates in one list without labels.
- Using left/right/front/back inconsistently.
- Mirroring a feature with guessed signs instead of using clear side functions.

## Side Naming

Use consistent naming:

- left: lower X side
- right: higher X side
- front: lower Y side
- back: higher Y side

This makes side-specific geometry and `side = -1 / 1` patterns easier to review.
