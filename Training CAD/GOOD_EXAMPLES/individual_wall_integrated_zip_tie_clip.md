# Good Example: Individual Wall-Integrated Zip-Tie Clip

Good design characteristics:

- compact isolated clip
- raised pad on the inside wall
- upper rounded horizontal slot
- lower rounded horizontal slot
- solid center bridge
- small side blends into the wall
- exterior wall remains solid
- zip tie can be fed from inside after the PCB is installed
- preview-only tie path validates serviceability

Recommended COMMAND LINK default:

```scad
wall_tie_count_per_side = 4;
wall_tie_y_positions_4 = [16, 32, 48, 64];
wall_tie_clip_width_y = 14;
wall_tie_clip_height_z = 15;
wall_tie_clip_projection = 3;
wall_tie_slot_width_y = 8;
wall_tie_slot_height_z = 2.7;
wall_tie_center_bridge_height = 4;
```

This avoids the ladder/rack visual while preserving useful strain-relief points.
