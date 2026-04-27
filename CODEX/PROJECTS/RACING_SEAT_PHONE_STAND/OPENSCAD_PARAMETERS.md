# OpenSCAD Parameters

Important parameters:

- `phone_width`
- `phone_thickness`
- `phone_height`
- `stand_width`
- `stand_depth`
- `stand_height`
- `seat_pan_width`
- `seat_pan_depth`
- `seat_pan_thickness`
- `seat_front_lip_h`
- `seat_side_lip_h`
- `backrest_angle`
- `backrest_y_offset`
- `backrest_height`
- `backrest_thickness`
- `backrest_bottom_width`
- `backrest_waist_width`
- `backrest_shoulder_width`
- `backrest_top_width`
- `slot_angle`
- `slot_depth`
- `slot_width`
- `enable_cable_cutout`
- `cable_cutout_size`
- `base_length`
- `base_width`
- `base_thickness`
- `base_rail_sep`
- `rollcage_width`
- `rollcage_depth`
- `rollcage_height`
- `rollcage_tube_d`

## V2 Parameters

Key V2 parameters:

- `mode`
- `render_id`
- `show_original_overlay`
- `show_reference_stl`
- `show_phone_placeholder`
- `show_exploded_view`
- `seat_width`
- `seat_height`
- `seat_depth`
- `seat_back_angle`
- `seat_pan_angle`
- `seat_shell_thickness`
- `seat_pan_thickness`
- `bolster_width`
- `bolster_height`
- `shoulder_bolster_width`
- `front_lip_height`
- `phone_slot_width`
- `phone_slot_depth`
- `phone_lean_angle`
- `phone_width`
- `phone_thickness`
- `phone_height`
- `rail_length`
- `rail_width`
- `rail_thickness`
- `rail_spacing`
- `rail_hole_diameter`
- `rail_hole_y_positions`
- `rail_boss_diameter`
- `truss_web_thickness`
- `rollcage_tube_radius`
- `brace_tube_radius`
- `rollcage_width`
- `rollcage_height`
- `rollcage_depth`

V2 SCAD path:

```text
C:\Users\LJ\OpenSCAD Projects\pre made traiing models 3d\racing seat phone stand\openscad_rebuild_v2\scad\racing_seat_phone_stand_v2.scad
```

## Photo Review Parameter Updates

The 2026-04-26 photo pass changed or added:

- `seat_back_angle = 17`
- `phone_lean_angle = 15`
- `photo_side_brace_bias = 0.86`

The pass also added named modules/wrappers for photo-guided intent:

- `photo_reference_target_notes()`
- `harness_opening_cutouts()`
- `seat_bolster_profile()`
- `trussed_side_rail()`
- `screw_boss_details()`

Use these parameters and modules when future tuning is based on reference photos.
