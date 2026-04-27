# COMMAND LINK PCB Standoff Bosses

## Source Facts

COMMAND LINK uses four real mounting holes:

```scad
mounting_hole_positions = [
    [2.600, 2.900],
    [62.190, 2.900],
    [2.600, 75.500],
    [62.190, 75.500]
];
```

The board is:

```scad
pcb_width = 65.000;
pcb_length = 78.710;
pcb_thickness = 1.600;
```

## Coordinate Mapping

Do not manually retype offsets. Map PCB-local coordinates into the enclosure:

```scad
pcb_origin_x = carrier_margin_left;
pcb_origin_y = carrier_margin_front;
function pcb_x(x) = pcb_origin_x + x;
function pcb_y(y) = pcb_origin_y + y;
```

## Heat-Set Insert Boss Logic

Each standoff should include:

- Standoff cylinder.
- Reinforced base pad.
- Insert pilot hole.
- Lead-in relief.
- Optional ribs or gussets.

The insert hole is a cut:

```scad
difference() {
    union() {
        cylinder(h = base_height, d = base_diameter);
        cylinder(h = standoff_height, d = standoff_outer_diameter);
    }
    translate([0, 0, insert_start])
        cylinder(h = insert_h, d = insert_hole_diameter);
}
```

## Screw Access

Add preview cylinders to show screwdriver access. If the access cylinder intersects a wall, wire feature, or lid feature, the design is not serviceable.

## Avoid

- Treating electrical solder pads as mounting holes.
- Placing bosses by guessed coordinates.
- Isolated skinny standoffs with no base support.
- Insert holes without enough surrounding material.
- Board guides that block board drop-in.

## Rule

PCB support geometry must be driven by actual PCB mounting coordinates and must remain serviceable with the PCB installed.
