# Good Example: Gear Machine Rebuild With Pitch Debug

## Good Pattern

A useful OpenSCAD gear-machine rebuild separates source facts from assumptions and makes the mechanical relationships visible.

Required review helpers:
- pitch circles for every gear
- vertical axis lines for shafts
- center-distance bars between meshing gears
- exploded view for stack order
- original STL overlay for individual parts
- cable/tape/material path preview when the machine routes material

## OpenSCAD Structure

Use modules like:
- `gear_tooth_profile()`
- `spur_gear_parametric()`
- `ring_gear_parametric()`
- `gear_mesh_preview()`
- `gear_center_debug()`
- `cable_path_preview()`
- `exploded_view()`

## Mechanical Checks

For external spur gears:
- pitch distance should be `(pitch_d_a + pitch_d_b) / 2`
- tooth count and pitch diameter should imply a consistent module
- gear axes should match source holes or shafts when available

For stacked gear trains:
- gears on the same shaft must share the same XY center
- gear planes must not collide with plates or collars
- stops/washers must leave clearance for rotation

## Acceptance Standard

The final render should explain how torque enters, how motion transfers through gears, and how the working feature moves.

