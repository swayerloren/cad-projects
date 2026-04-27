# COMMAND_LINK Facts

## Confirmed Source Path

Actual project source folder:

```text
C:\Users\LJ\OpenSCAD Projects\command link
```

## Confirmed PCB Facts

| Item | Value | Source |
|---|---:|---|
| PCB width, X | 65.000 mm | `PCB_MECHANICAL_ANALYSIS.md`, Edge.Cuts centerline |
| PCB length, Y | 78.710 mm | `PCB_MECHANICAL_ANALYSIS.md`, Edge.Cuts centerline |
| PCB thickness | 1.600 mm | KiCad PCB `(general (thickness ...))` |
| Board shape | Rectangular | Edge.Cuts `gr_rect` |
| Board corner radius | 0 mm / not modeled | No Edge.Cuts arcs |
| Tallest top component | 10.50 mm above PCB | C11 `CP_Elec_8x10.5`, local STEP/model basis |
| Top-side footprints | 46 | Mechanical analysis |
| Bottom-side footprints | 0 | Mechanical analysis / bottom pick-and-place |

## Confirmed Mounting Holes

The mechanical mounting holes are large circular netless holes represented as top-level plated vias in the PCB, not separate NPTH mounting footprints.

| ID | PCB-local X | PCB-local Y | Drill | Pad/via diameter | Recommended screw |
|---|---:|---:|---:|---:|---|
| MH1 | 2.600 mm | 2.900 mm | 3.200 mm | 4.000 mm | M3 |
| MH2 | 62.190 mm | 2.900 mm | 3.200 mm | 4.000 mm | M3 |
| MH3 | 2.600 mm | 75.500 mm | 3.200 mm | 4.000 mm | M3 |
| MH4 | 62.190 mm | 75.500 mm | 3.200 mm | 4.000 mm | M3 |

## Confirmed Wire / Solder Pad Zones

| Ref | Location | Board-local zone | Notes |
|---|---|---|---|
| J4 | Left side | Y about 10 to 38 mm | 4 solder-wire pads |
| J3 | Left side | Y about 41 to 69 mm | 4 solder-wire pads |
| J2 | Right side | Y about 18 to 62 mm | 6 solder-wire pads |
| J1 | Top side | Center near X 32.320, Y 66.365 mm | 1x06 programming header |

The solder-wire footprint descriptions specify 2 mm conductor, 3.9 mm outer diameter wire, and bend radius of 3x OD.

## Confirmed Current OpenSCAD Facts

From `openscad_pcb_carrier\command_link_rugged_enclosure.scad`:

| Parameter | Value |
|---|---:|
| `pcb_width` | 65.000 |
| `pcb_length` | 78.710 |
| `pcb_thickness` | 1.600 |
| `pcb_tallest_top_component` | 10.5 |
| `compact_side_clearance_mode` | `true` |
| `compact_side_margin` | 14.25 |
| `carrier_margin_left` | `compact_side_margin` |
| `carrier_margin_right` | `compact_side_margin` |
| `carrier_margin_front` | 10 |
| `carrier_margin_back` | 10 |
| `floor_thickness` | 4.0 |
| `wall_thickness` | 3.5 |
| `wall_height` | 20.0 |
| `top_rim_height` | 0.9 |
| `top_rim_overhang` | 0.35 |
| `wall_inner_corner_radius` | 1.5 |
| `standoff_height` | 5.0 |
| `standoff_outer_diameter` | 7.0 |
| `insert_hole_diameter` | 4.2 |
| `insert_depth` | 5.0 |
| `main_grommet_hole_diameter` | 16.0 |
| `main_grommet_side` | `front` |
| `grommet_outer_flange_diameter` | 24.0 |
| `grommet_clearance_margin` | 2.0 |
| `grommet_boss_outer_diameter` | 28.0 |
| `grommet_boss_thickness` | 3.0 |
| `grommet_boss_face_diameter` | 24.0 |
| `grommet_boss_face_height` | 0.8 |
| `grommet_hole_edge_chamfer` | 0.8 |
| `wall_tie_count_per_side` | 4 |
| `wall_tie_y_positions_4` | `[14,30,52,68]` |
| `wall_tie_slot_width_y` | 8.0 |
| `wall_tie_slot_height_z` | 2.7 |
| `wall_tie_center_bridge_height` | 4.0 |
| `wall_tie_clip_width_y` | 14.0 |
| `wall_tie_clip_height_z` | 15.0 |
| `wall_tie_projection` | 2.5 |
| `wall_tie_pad_projection` | 2.5 |
| `wall_tie_strip_enabled` | `false` |
| `wire_lane_clearance_from_pcb` | 2.0 |
| `wire_lane_width` | 6.0 |
| `wire_lane_to_tie_clearance` | 0.25 |
| `zip_tie_band_width` | 4.0 |
| `zip_tie_band_thickness` | 1.4 |
| `mount_hole_diameter` | 4.2 |
| `mount_boss_outer_diameter` | 11.0 |
| `mount_ear_thickness` | 5.0 |
| `mount_ear_length` | 20.0 |
| `mount_ear_width` | 14.0 |

## Assumptions

| Assumption | Current Value / Basis |
|---|---|
| PCB screws | M3, based on 3.2 mm mounting holes |
| PCB heat-set insert pilot | 4.2 mm default, must be verified with actual inserts |
| Insert depth | 5.0 mm default, must be verified with actual inserts |
| Main wire entry | One 16 mm circular short-side grommet/cable-gland hole |
| Grommet side | Front short side by default |
| Print material | PETG, ASA, ABS, nylon, or similar preferred for UTV environment |
| Future relay board | Not modeled; placeholder features remain disabled |
