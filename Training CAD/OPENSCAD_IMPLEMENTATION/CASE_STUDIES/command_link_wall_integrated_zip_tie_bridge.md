# COMMAND LINK Case Study: Wall-Integrated Zip-Tie Bridge

## Design Goal

Create an internal wall-integrated cable-tie feature that can be used after PCB installation without cutting through the exterior enclosure wall.

## Accepted Shape

The inside wall face should read as:

```text
[ smooth upper horizontal slot ]
[ rounded solid center bridge ]
[ smooth lower horizontal slot ]
```

The zip tie feeds through the upper and lower slots from inside the enclosure, wraps around the center bridge, and loops around the wire bundle.

## Key Rules

- Keep the exterior wall solid.
- Limit slot cut depth to the inward pad/bridge body.
- Use rounded or chamfered slot mouths.
- Avoid stacked rectangular blocks.
- Avoid continuous hard rails when individual service features are clearer.
- Keep the features visible and reachable after PCB installation.

## Useful Parameters

```scad
wall_tie_slot_width = 7.0;
wall_tie_slot_height = 2.4;
wall_tie_vertical_gap = 3.5;
wall_tie_pad_width = 12.0;
wall_tie_pad_height = 13.0;
wall_tie_pad_projection = 2.0;
wall_tie_edge_radius = 1.0;
wall_tie_slot_chamfer = 0.6;
wall_tie_center_bridge_rounding = 0.8;
```

## Review Checklist

- Six usable bridges per long side when that is the design requirement.
- Upper and lower slots are visible from inside.
- The tie path preview shows a physical route.
- PCB and solder pads remain serviceable.
- Exterior wall has no tie-slot leak path.

