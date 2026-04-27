# OpenSCAD Parameters

Current source:

```text
C:\Users\LJ\OpenSCAD Projects\my projects\command link\openscad_pcb_carrier\command_link_rugged_enclosure.scad
```

## Mode / Export Parameters

| Parameter | Current Value | Purpose | If Increased | If Decreased |
|---|---:|---|---|---|
| `mode` | `"preview"` | Selects preview, production, or cutaway behavior | N/A | N/A |
| `is_preview` | `mode == "preview"` | Gates all helper geometry | N/A | N/A |
| `is_production` | `mode == "production"` | Documents production export mode | N/A | N/A |
| `is_cutaway` | `mode == "cutaway"` | Optional debug cutaway mode | N/A | N/A |

## PCB Parameters

| Parameter | Current Value | Purpose | If Increased | If Decreased |
|---|---:|---|---|---|
| `pcb_width` | 65.000 | Confirmed board X size | Placeholder and feature mapping become too wide | Board may not fit |
| `pcb_length` | 78.710 | Confirmed board Y size | Placeholder and feature mapping become too long | Board may not fit |
| `pcb_thickness` | 1.600 | Board thickness | Raises top reference if used in stack calculations | Underestimates clearances |
| `pcb_tallest_top_component` | 10.5 | Tallest top component height | Adds conservative component clearance context | May under-protect tall components |
| `mounting_hole_positions` | `[2.600,2.900]`, `[62.190,2.900]`, `[2.600,75.500]`, `[62.190,75.500]` | PCB mounting/standoff coordinates | Do not change unless PCB changes | Do not change unless PCB changes |

## Body And Wall Parameters

| Parameter | Current Value | Purpose | If Increased | If Decreased |
|---|---:|---|---|---|
| `compact_side_clearance_mode` | `true` | Uses calculated compact side margins for wire/tie service lane | Uses computed compact lane when true | Falls back to 26 mm side margins when false |
| `compact_side_margin` | 14.4 | Calculated side margin from wall, tie pad, wire lane, and PCB clearance | More wire/service room if inputs increase | Tighter fit if inputs decrease |
| `carrier_margin_left` | `compact_side_margin` | Left PCB margin and wall-integrated zip-tie bridge clearance | More wire/service room, larger body | Tighter fit, less routing room |
| `carrier_margin_right` | `compact_side_margin` | Right PCB margin and wall-integrated zip-tie bridge clearance | More wire/service room, larger body | Tighter fit, less routing room |
| `carrier_margin_front` | 10 | Front PCB margin | More grommet/wire room, longer body | Less grommet and wire bend room |
| `carrier_margin_back` | 10 | Back PCB margin | More service room, longer body | Less clearance |
| `floor_thickness` | 4.0 | Rugged enclosure base thickness | Stronger but heavier/slower print | Weaker floor |
| `wall_thickness` | 3.5 | Perimeter wall thickness | Stronger walls, more material | Weaker walls |
| `wall_height` | 20.0 | Protective side wall height | More side protection | Less board/wire protection |
| `wall_inner_corner_radius` | 1.5 | Rounded inner corner radius for continuous shell | Softer internal corners | Sharper internal corners |
| `top_rim_height` | 0.9 | Height of molded top rim cap | More visible rim, taller exterior | Lower/subtler rim |
| `top_rim_width` | `wall_thickness + 0.7` | Width of top rim cap | Wider rim, slightly more top opening overlap | Narrower rim |
| `top_rim_overhang` | 0.35 | Small rim overhang beyond wall faces | Softer edge, larger exterior lip | More flush rim |
| `top_rim_corner_radius` | 1.4 | Rim edge rounding | Softer rim | Sharper rim |
| `molded_feature_radius` | 1.0 | Common radius for small internal features | Softer molded features | Sharper features |
| `rib_corner_radius` | 0.7 | Common radius for low reinforcement ribs | Softer rib edges | Sharper rib edges |

## Manufacturing Cleanup Parameters

| Parameter | Current Value | Purpose | If Increased | If Decreased |
|---|---:|---|---|---|
| `edge_chamfer` | 0.8 | General small edge softening intent for pads, guides, and low ribs | Softer transitions, possible slower render if used in complex helpers | Sharper features |
| `large_edge_chamfer` | 1.5 | Larger transition intent for mount roots and heavier features | Larger molded blends | Smaller transitions |
| `rim_chamfer_size` | 1.0 | Top rim chamfer/softening intent | Softer rim if geometry allows | Sharper rim |
| `slot_edge_chamfer` | 0.5 | Zip-tie slot-mouth softening value | Easier tie feed, more slot mouth relief | Sharper slot edges |
| `mount_transition_radius` | 2.0 | External mount neck/transition radius target | Softer mount root | Sharper mount root |
| `boss_blend_radius` | 1.5 | Tapered blend under external mount bosses | Wider boss root, more material | More abrupt boss |
| `grommet_boss_blend_radius` | 1.5 | Tapered blend where grommet boss meets wall | Smoother grommet boss transition | More abrupt boss |
| `molding_draft_angle_preview` | 1.5 | Documentation/review target for future molded draft | More conservative draft target | Less draft target |

## PCB Mounting / Insert Parameters

| Parameter | Current Value | Purpose | If Increased | If Decreased |
|---|---:|---|---|---|
| `standoff_height` | 5.0 | PCB height above floor | More bottom clearance | Less solder/pin clearance |
| `standoff_outer_diameter` | 7.0 | PCB standoff strength | Stronger boss, less nearby clearance | Weaker boss |
| `standoff_base_diameter` | 13.0 | Reinforced standoff base | Better load spread | Less floor support |
| `insert_hole_diameter` | 4.2 | Heat-set insert pilot | Looser insert fit | Tighter insert fit, possible splitting |
| `insert_depth` | 5.0 | Insert seating depth | More insert depth | Insert may bottom out or not seat |
| `insert_top_relief_diameter` | 4.9 | Lead-in relief | Easier insert start | Less lead-in |
| `insert_top_relief_depth` | 0.8 | Lead-in relief depth | More lead-in | Less lead-in |

## Grommet / Cable Entry Parameters

| Parameter | Current Value | Purpose | If Increased | If Decreased |
|---|---:|---|---|---|
| `main_grommet_hole_diameter` | 16.0 | Circular wire entry hole | Fits larger grommet/cable gland, weakens wall more | Fits smaller grommet, less wire room |
| `main_grommet_side` | `front` | Selects front/back short-side entry | Use `back` to move entry to rear | Use `front` for current default |
| `main_grommet_center_x` | `enclosure_width / 2` | Centers grommet across body width | Offset if needed for cable routing | Offset opposite direction |
| `main_grommet_center_z` | `floor_thickness + wall_height / 2` | Centers grommet vertically in wall | Moves hole upward | Moves hole downward |
| `grommet_outer_flange_diameter` | 24.0 | Preview target for outside rubber grommet flange | Larger flange target | Smaller flange target |
| `grommet_inner_flange_diameter` | 24.0 | Preview target for inside rubber grommet flange | Larger flange target | Smaller flange target |
| `grommet_flange_thickness` | 3.0 | Preview flange thickness | Thicker flange preview | Thinner flange preview |
| `grommet_clearance_margin` | 2.0 | Radial landing margin around the 24 mm flange | Larger landing boss | Less landing margin |
| `grommet_hole_edge_chamfer` | 0.8 | Production chamfer at hole mouths | Softer rubber contact edge | Sharper hole edge |
| `grommet_boss_enabled` | `true` | Enables reinforcing boss/ring | Adds support if true | Removes boss if false |
| `grommet_boss_outer_diameter` | 28.0 | Boss outside diameter / landing for 24 mm flange plus margin | Stronger grommet area | Less support |
| `grommet_boss_thickness` | 3.0 | Boss projection/thickness | More grommet support | Less grommet support |
| `grommet_boss_face_diameter` | 24.0 | Raised face/ring at grommet flange target | Larger visible face ring | Smaller, subtler face ring |
| `grommet_boss_face_height` | 0.8 | Raised face height within total boss thickness | More pronounced stepped boss | Flatter boss |
| `cable_gland_nut_diameter` | 28.0 | Optional gland nut preview diameter | Larger nut preview | Smaller nut preview |
| `cable_gland_nut_thickness` | 5.0 | Optional gland nut preview thickness | Thicker nut preview | Thinner nut preview |
| `show_grommet_hardware_preview` | `true` | Shows grommet flange and grip envelope in preview | N/A | Hides preview |
| `show_cable_gland_preview` | `false` | Shows optional gland nut envelope in preview | N/A | Hides preview |
| `show_wire_bend_clearance_preview` | `true` | Shows wire bend clearance envelope in preview | N/A | Hides preview |
| `wire_bundle_diameter_preview` | 8.0 | Preview wire bundle diameter for grommet routing | Larger harness preview | Smaller harness preview |
| `wire_min_bend_radius_preview` | 24.0 | 3x wire bundle bend radius preview target | Larger bend envelope | Smaller bend envelope |

## Zip-Tie Slot Status / Wire Routing Parameters

Current removal update:

- `show_zip_tie_features = false`
- `show_old_zip_tie_rack = false`
- `show_zip_tie_path_preview = false`
- `show_wall_tie_cutout_preview = false`
- `show_slot_cutout_preview = false`
- `show_wall_tie_clip_preview_path = false`
- `show_wall_tie_clip_cutout_preview = false`
- `show_wire_bundle_preview = false`

All generated zip-tie slot, bridge, rack, clip, cutout-preview, and tie-path preview geometry is inactive by default. The user will add the final zip-tie slots manually later.

| Parameter | Current Value | Purpose | If Increased | If Decreased |
|---|---:|---|---|---|
| `show_zip_tie_features` | `false` | Master gate for legacy/generated zip-tie geometry | Only enable if explicitly requested | Keeps side walls solid |
| `show_zip_tie_path_preview` | `false` | Legacy translucent zip-tie band path preview | Do not enable unless slots are restored | Keeps preview free of tie helpers |
| `show_wall_tie_cutout_preview` | `false` | Legacy wall-tie cutout preview | Do not enable unless slots are restored | Keeps preview free of tie helpers |
| `show_slot_cutout_preview` | `false` | Legacy slot-opening preview | Do not enable unless slots are restored | Keeps preview free of tie helpers |
| `show_wire_bundle_preview` | `false` | Legacy tie/wire bundle preview near side wall | Do not enable unless service slots are restored | Keeps preview free of tie helpers |
| `show_service_clearance_preview` | `false` | Legacy side service clearance preview | Do not enable unless service slots are restored | Keeps preview free of tie helpers |
| `wire_lane_clearance_from_pcb` | 2.5 | Gap from PCB edge to wire lane | More solder/board clearance, wider body | Tighter to PCB |
| `wire_lane_width` | 6.0 | Usable side lane for wire bundle | More wire room, wider body | Less wire room |
| `wire_lane_to_tie_clearance` | 0.4 | Small gap between wire lane and wall-tie pad | More clearance, wider body | Tighter lane-to-pad spacing |
| `wall_tie_count_per_side` | 4 | Number of wall-integrated clips on each long side | More tie points, more clutter | Fewer strain relief points |
| `wall_tie_y_positions` | `[11,22,33,44,55,66]` | PCB-local Y positions for each side's wall bridge features | Move/space tie points differently | Move/space tie points differently |
| `wall_tie_projection` | 2.0 | Effective slot/tie bridge depth target | More tie-path depth | Lower profile |
| `wall_tie_pad_projection` | 2.0 | How far the pad protrudes inward from wall | More slot depth/material | Lower profile |
| `wall_tie_slot_width` | 7.0 | Horizontal inside-facing slot length along Y | Fits wider ties/easier threading | Less slot room |
| `wall_tie_slot_height` | 2.4 | Vertical opening height for each slot | Fits thicker ties/print variation | May become unthreadable |
| `wall_tie_vertical_gap` | 3.5 | Solid center bridge between upper/lower slots | Stronger center bridge | Less bridge material |
| `wall_tie_pad_width` | 12.0 | Molded pad width along Y | More material and easier access | More compact |
| `wall_tie_pad_height` | 13.0 | Molded pad height on wall | More vertical slot/bridge room | More compact |
| `wall_tie_back_thickness` | 2.5 | Minimum closed exterior backing target; current cuts leave full wall thickness behind pad | More conservative wall backing target | Less backing target |
| `wall_tie_edge_radius` | 1.0 | Rounded pad perimeter radius | Softer molded pad outline | Sharper pad |
| `wall_tie_slot_chamfer` | `slot_edge_chamfer` | Rounded/chamfered slot mouth size | Easier tie feed and smoother look | Sharper slot edges |
| `wall_tie_center_bridge_rounding` | 0.8 | Front bridge skin/rounding target | Rounder center bridge | Flatter bridge |
| `wall_tie_side_blend_enabled` | `true` | Adds local side blends per pad | More molded transition | Simpler isolated pad |
| `wall_tie_chamfer` | `wall_tie_edge_radius` | Backward-compatible pad edge softening alias | Softer molded appearance | Sharper pad |
| `wall_tie_strip_enabled` | `false` | Continuous strip is disabled to avoid hard-rail appearance | More continuous wall rail if true | Individual molded pads |
| `wall_tie_strip_height` | 1.2 | Vertical height of subtle tie strip | More visible strip | Subtler strip |
| `wall_tie_strip_thickness` | 0.65 | Inward projection of subtle tie strip | Stronger/more visible strip | Lower profile |
| `zip_tie_band_width` | 4.0 | Nominal small zip-tie band width | Matches wider tie if increased | Matches narrower tie |
| `zip_tie_band_thickness` | 1.4 | Nominal small zip-tie band thickness | Matches thicker tie if increased | Matches thinner tie |
| `wire_bundle_diameter_preview` | 4.0 | Diameter used for translucent wire bundle previews | Shows larger bundle | Shows smaller bundle |
| `wire_landing_height` | 1.3 | Low raised wire landing pad height | More wire support | Flatter floor |
| `wire_trunk_width` | 13.0 | Central wire trunk width from grommet | More bundle room | Less wire room |
| `wire_guard_width` | 2.2 | Low guide/guard width | Stronger guide | More compact |
| `wire_guard_height` | 5.2 | Low guide/guard height | More wire guidance | Lower guide |

Audit notes:

- `zip_tie_slot_array_cutouts()` is still present but exits unless `show_zip_tie_features` is true.
- The production STL should contain no zip-tie slots with the default parameter set.
- Older wall-tie parameters remain historical/reference values only while `show_zip_tie_features = false`.
- Production export must use `mode="production"` so preview helpers are not included in the STL.

## Refined Mount Ear Parameters

| Parameter | Current Value | Purpose | If Increased | If Decreased |
|---|---:|---|---|---|
| `mount_ear_length` | 18.0 | Outboard length of each external rounded ear | More screw distance and washer room | More compact but less mount area |
| `external_mount_style` | `"simple_integrated_ear"` | Active external mount style | N/A | N/A |
| `show_old_external_mounts` | `false` | Keeps rejected old mount layout disabled | Shows old layout for comparison only | Keeps production target active |
| `mount_ear_width` | 16.0 | Ear width along the enclosure side | More load spread around fastener | More compact but less support |
| `mount_ear_thickness` | 5.0 | Main lug thickness | Stronger clamp area | More flexible mount |
| `mount_hole_diameter` | 4.3 | External mount screw clearance | Fits larger screw | Tighter screw clearance |
| `mount_boss_outer_diameter` | 10.0 | Raised boss/ring around screw hole | Better washer/load support | Less clamp support |
| `mount_boss_height` | 1.5 | Low raised boss height | More screw/washer bearing height | Lower boss |
| `mount_boss_chamfer` | 0.8 | Taper/chamfer on low boss | Softer boss edge | Sharper boss edge |
| `mount_neck_width` | 16.0 | Wide blended neck into wall/floor | Stronger root connection | Weaker root connection |
| `mount_neck_length` | 8.0 | Wall/floor overlap region | More load transfer | More compact root |
| `mount_neck_blend_radius` | 3.0 | Root blend radius | Softer transition | Sharper transition |
| `mount_gusset_enabled` | `true` | Enables simple side gussets | Adds support | Removes rib support |
| `mount_gusset_thickness` | 3.0 | Clean gusset thickness | Stronger gussets | Weaker gussets |
| `mount_gusset_height` | 7.0 | Gusset height above lug | Stiffer root support | Lower stiffness |
| `mount_gusset_length` | 10.0 | Gusset reach from wall toward boss | Longer load path | Shorter load path |
| `mount_edge_chamfer` | 0.8 | Top edge softening on ear body | Softer printed edge | Sharper printed edge |
| `mount_edge_rounding` | 3.0 | Legacy alias for root/neck rounding | Softer transitions | Sharper transitions |
| `mount_ear_edge_margin` | 4.0 | Distance from body end to each ear | More end clearance | Closer to corner |

## Future Relay Board Parameters

| Parameter | Current Value | Purpose | If Increased | If Decreased |
|---|---:|---|---|---|
| `show_future_relay_features` | `false` | Future upper relay support toggle | Shows placeholder posts if true | Keeps relay features disabled |
| `future_relay_post_diameter` | 7.0 | Placeholder post diameter | Stronger future post | Smaller future post |
| `future_relay_post_height` | 24.0 | Placeholder post height | More stack height | Less stack height |
| `future_relay_insert_hole_diameter` | 3.2 | Future insert/screw hole | Larger future hole | Smaller future hole |

## Rugged Lid Parameters

Source:

```text
C:\Users\LJ\OpenSCAD Projects\my projects\command link\openscad_pcb_carrier\command_link_rugged_lid.scad
```

| Parameter | Current Value | Purpose |
|---|---:|---|
| `lid_top_thickness` | 3.5 | Rugged lid panel thickness |
| `lid_side_overhang` | 2.0 | Lid overhang past lower body footprint |
| `lid_corner_radius` | 4.0 | Rounded lid corners |
| `seal_enabled` | `true` | Enables O-ring groove cut |
| `oring_cross_section_diameter` | 2.0 | Nominal O-ring size assumption |
| `oring_groove_width` | 2.6 | Printed O-ring groove width |
| `oring_groove_depth` | 1.4 | Printed O-ring groove depth |
| `oring_compression_percent` | 20 | Target compression for documentation/testing |
| `lid_sealing_lip_depth` | 3.0 | Downward lip depth |
| `lid_sealing_lip_clearance` | 0.35 | Clearance to lower wall opening |
| `lid_fastener_count` | 6 | Lid-to-base screw count |
| `lid_screw_clearance_diameter` | 3.4 | M3 lid screw clearance |
| `lid_insert_hole_diameter` | 4.2 | Future lower base insert pilot target |
| `lid_insert_depth` | 5.0 | Future lower base insert depth target |
| `relay_count` | 5 | Relay mount zones |
| `relay_placeholder_width` | 28.0 | Assumed relay footprint width |
| `relay_placeholder_depth` | 28.0 | Assumed relay footprint depth |
| `relay_placeholder_height` | 32.0 | Assumed relay body height |
| `relay_bracket_screw_spacing` | 22.0 | Two insert bosses per relay |
| `relay_bracket_insert_hole_diameter` | 4.2 | Relay bracket insert pilot |
| `relay_bracket_boss_od` | 7.0 | Relay bracket boss outer diameter |
| `relay_bracket_boss_height` | 5.5 | Relay bracket boss height |

## Shared Base/Lid Mating Parameters

Source:

```text
C:\Users\LJ\OpenSCAD Projects\my projects\command link\openscad_pcb_carrier\command_link_shared_dimensions.scad
```

| Parameter | Current Value | Purpose |
|---|---:|---|
| `shared_lid_fastener_edge_offset` | 6.0 | Shared six-position lid/base fastener offset |
| `shared_lid_screw_clearance_diameter` | 3.4 | M3 lid screw clearance |
| `shared_base_lid_insert_hole_diameter` | 4.2 | M3 heat-set insert pilot in lower base |
| `shared_base_lid_insert_depth` | 5.0 | Blind insert hole depth in lower base |
| `shared_base_lid_insert_boss_od` | 7.0 | Lower-base lid insert boss outside diameter |
| `shared_base_lid_insert_boss_height` | 6.0 | Reinforced top collar height for insert boss |
| `shared_oring_cross_section_diameter` | 2.0 | Nominal O-ring cross-section |
| `shared_oring_groove_width` | 2.6 | Lid underside O-ring groove width |
| `shared_oring_groove_depth` | 1.4 | Lid underside O-ring groove depth |
| `shared_base_sealing_land_width` | 3.2 | Base-side sealing land width |
| `shared_base_sealing_land_height` | 0.8 | Base-side raised land height |
| `shared_base_lid_fit_clearance` | 0.35 | Lid/base fit clearance target |

## Sidewall Service Spine Parameters

| Parameter | Current Value | Purpose |
|---|---:|---|
| `shared_wire_lane_clearance_from_pcb` | 2.0 | PCB edge clearance before the wire lane |
| `shared_wire_lane_width` | 6.0 | Nominal side wire lane width |
| `shared_wire_lane_to_tie_clearance` | 0.25 | Compact transition between wire lane and clip/spine |
| `shared_wall_tie_pad_projection` | 2.5 | Zip-tie clip projection into the enclosure |
| `shared_side_spine_enabled` | `true` | Enables integrated side-wall service spine |
| `shared_side_spine_width` | 6.0 | Side-wall spine width/projection zone |
| `shared_side_spine_height` | 21.7 | Full-height side-wall spine height |
| `shared_wall_integrated_lid_boss_enabled` | `true` | Uses wall-integrated lid insert bosses |
| `shared_wall_lid_boss_od` | 7.0 | Wall-integrated lid insert boss OD |
| `shared_wall_lid_boss_projection` | 2.5 | Insert boss center projection target |
| `shared_wall_lid_boss_insert_hole_diameter` | 4.2 | M3 insert pilot diameter |
| `shared_wall_lid_boss_insert_depth` | 5.0 | M3 insert pilot depth |
## Base/Lid Shared Fit Parameters - 2026-04-26

Shared source file:

```text
my projects/command link/openscad_pcb_carrier/command_link_shared_dimensions.scad
```

Key shared values:

| Parameter | Value |
|---|---:|
| `shared_pcb_width` | 65.0 mm |
| `shared_pcb_length` | 78.71 mm |
| `shared_floor_thickness` | 4.0 mm |
| `shared_wall_thickness` | 3.5 mm |
| `shared_wall_height` | 20.0 mm |
| `shared_top_rim_height` | 0.9 mm |
| `shared_lid_fastener_edge_offset` | 6.0 mm |
| `shared_lid_screw_clearance_diameter` | 3.4 mm |
| `shared_base_lid_insert_hole_diameter` | 4.2 mm |
| `shared_base_lid_insert_depth` | 5.0 mm |
| `shared_oring_cross_section_diameter` | 2.0 mm |
| `shared_oring_groove_width` | 2.6 mm |
| `shared_oring_groove_depth` | 1.4 mm |
| `shared_base_sealing_land_width` | 3.2 mm |
| `shared_base_sealing_land_height` | 0.8 mm |
| `shared_lid_sealing_lip_depth` | 3.0 mm |
| `shared_lid_sealing_lip_clearance` | 0.35 mm |

Derived checks:

- `command_link_body_width()` = 93.5 mm.
- `command_link_body_length()` = 98.71 mm.
- `command_link_base_lid_seat_z()` = 25.68 mm.
- `command_link_lid_fastener_positions_default()` returns the six shared M3 lid fastener positions.

## Relay Bracket Shared Parameters - 2026-04-26

Shared source file:

```text
my projects/command link/openscad_pcb_carrier/command_link_relay_layout_dimensions.scad
```

| Parameter | Value |
|---|---:|
| `shared_relay_count` | 5 |
| `shared_relay_body_width` | 28.0 mm |
| `shared_relay_body_depth` | 28.0 mm |
| `shared_relay_body_height` | 32.0 mm |
| `shared_relay_spacing` | 6.0 mm |
| `shared_relay_layout_request` | `single_row` |
| resolved layout | `staggered_3_2` for the compact lid |
| `shared_relay_bracket_screw_spacing` | 22.0 mm |
| `shared_relay_bracket_screw_clearance_diameter` | 3.4 mm |
| `shared_relay_bracket_screw_head_clearance_diameter` | 6.5 mm |
| `shared_relay_bracket_wall_thickness` | 2.5 mm |
| `shared_relay_bracket_base_thickness` | 3.0 mm |
| `shared_relay_bracket_height` | 14.0 mm |
| `shared_relay_bracket_capture_depth` | 8.0 mm |
| `shared_relay_capture_lip_height` | 2.5 mm |
| `shared_relay_capture_lip_depth` | 2.0 mm |
| `shared_relay_rubber_pad_allowance` | 1.0 mm |

Bracket export source:

```text
my projects/command link/openscad_pcb_carrier/command_link_relay_brackets.scad
```

## Grommet Inside Collar Relief Parameters - 2026-04-26

Active file:

```text
my projects/command link/openscad_pcb_carrier/command_link_rugged_enclosure.scad
```

| Parameter | Value |
|---|---:|
| `main_grommet_hole_diameter` | 16.0 mm |
| `grommet_inner_flange_diameter` | 24.0 mm |
| `grommet_clearance_margin` | 2.0 mm |
| `inside_grommet_clearance_diameter` | 28.0 mm |
| `inside_grommet_clearance_depth` | 5.0 mm |
| `inside_grommet_landing_flat_depth` | 3.5 mm |
| `inside_grommet_relief_enabled` | `true` |

The relief starts at the inside wall face and cuts inward only. It is intended
to remove wire-rail/rib interference behind the grommet collar without cutting
through the exterior wall.

## Lid Seal Keepout / Relay Clamp Parameters - 2026-04-27

Active files:

```text
my projects/command link/openscad_pcb_carrier/command_link_shared_dimensions.scad
my projects/command link/openscad_pcb_carrier/command_link_relay_layout_dimensions.scad
my projects/command link/openscad_pcb_carrier/command_link_rugged_lid.scad
my projects/command link/openscad_pcb_carrier/command_link_relay_brackets.scad
```

| Parameter | Value |
|---|---:|
| `shared_seal_keepout_width` | 8.0 mm |
| `shared_lid_seating_keepout_width` | 8.0 mm |
| `shared_lid_wall_clearance` | 0.45 mm |
| `shared_lid_vertical_seating_clearance` | 0.35 mm |
| `shared_relay_keepout_from_oring` | 8.0 mm target |
| `shared_relay_layout_request` | `compact_3_2` |
| `relay_clamp_type` | `open_bottom_top_bridge` |
| `relay_clamp_bridge_width` | 10.0 mm |
| `relay_clamp_bridge_thickness` | 3.0 mm |
| `relay_clamp_foot_length` | 9.0 mm |
| `relay_clamp_foot_width` | 8.0 mm |
| `relay_clamp_foot_thickness` | 3.0 mm |

Note: five assumed 28 mm relay bodies are packaging-constrained. Insert holes
are pulled clear of the seal channel, but the relay body envelope remains a
hardware-measurement item.

## Cable Gland Inner Nut Clearance Parameters - 2026-04-27

Active file:

```text
my projects/command link/openscad_pcb_carrier/command_link_rugged_enclosure.scad
```

| Parameter | Value |
|---|---:|
| `main_wire_entry_type` | `cable_gland` |
| `main_grommet_hole_diameter` | 16.0 mm |
| `cable_gland_thread_diameter` | 16.0 mm |
| `cable_gland_outer_flange_diameter` | 24.0 mm |
| `cable_gland_inner_nut_diameter` | 28.0 mm |
| `cable_gland_inner_nut_thickness` | 5.0 mm |
| `cable_gland_tool_clearance_diameter` | 34.0 mm |
| `inside_fitting_clearance_diameter` | 34.0 mm |
| `inside_fitting_clearance_depth` | 8.0 mm |
| `inside_flat_landing_diameter` | 32.0 mm |
| `relief_width_along_wall` | 38.0 mm |

The inside relief is a real production cut. The cable gland nut, tool
clearance, and wire bend bodies are preview-only helpers and must not export in
production mode.
