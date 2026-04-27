# Errors And Fixes

## 1. Flat Carrier Tray

Error:

The initial carrier was only a flat tray with no walls.

Fix:

Redesign as a rugged lower enclosure / protected carrier.

## 2. Standalone Zip-Tie Posts

Error:

Zip-tie anchors were standalone posts.

Fix:

Integrate strain relief into internal wall/floor features.

## 3. Through-Wall Zip-Tie Slots

Error:

Zip-tie slots cut through the exterior wall.

Fix:

Zip-tie features must be internal-only and must not create exterior leak paths.

## 4. Rectangular Side Wire Opening

Error:

Wire entry was a long rectangular side opening.

Fix:

Use one circular grommet/cable-gland hole on a short side.

## 5. Weak Flat External Mounting Tabs

Error:

External mounting tabs were weak flat ears.

Fix:

Use reinforced mount pods with bosses, triangular gussets, ribs, and proper load paths.

## 6. Blocky Internal Zip-Tie Mounts

Error:

Internal zip-tie mounts looked like stacked rectangular blocks and did not resemble molded automotive cable-management features.

Fix:

Replace them with clean internal cable-tie saddle mounts: low floor pads, smooth raised rails, usable tie tunnels, rounded/chamfered edges, and no exterior wall holes.

## 7. Ugly Non-OEM External Mount Pods

Error:

The reinforced external mount pods became visually rough, chunky, and non-OEM, with truss fins that looked like random bracket geometry.

Fix:

Replace them with clean rounded automotive-style mounting ears: rounded lug shape, raised circular screw boss, broad neck into the wall, and a small number of clean gussets.

## 8. Crude Rounded Mount Ears

Error:

The first rounded external ears still looked too patched-on and not production-ready.

Fix:

Refine the ears into molded oval/teardrop-style lugs with centered screw holes, raised bosses, wider wall/floor necks, and two clean load-path gussets per ear.

## 9. Crude Internal Saddle Geometry

Error:

The internal cable-tie mounts still looked crude and did not read like molded production strain-relief features.

Fix:

Replace the old rail/block saddle geometry with low wall-side wire lanes and compact bridge-style cable-tie saddles with rounded bases, real pass-under tunnels, and small lead-in gussets.

## 10. Fake / Unusable Cable-Tie Saddles

Error:

The previous saddle geometry still did not provide a clearly usable physical zip-tie path. A real tie needed to enter one side, pass through a visible tunnel, exit the other side, then loop over the wire bundle.

Fix:

Replace the three old saddle features with twelve floor-mounted internal cable-tie bridge slots: six per PCB long side. Each feature uses raised side feet, a top bridge, and a real rectangular tunnel. The exterior wall remains solid.

## 11. Trapped / Non-Serviceable Zip-Tie Saddles

Error:

The twelve bridge features were too close to the PCB and side pad zones. After PCB installation, a real zip tie could not be easily threaded through the features without working blindly behind the board.

Fix:

Replace the trapped side-channel bridge geometry with open-top serviceable cable-tie saddles in the side channels. Each saddle must remain accessible from above after PCB installation, with clearance from the PCB edge and inside wall, visible tie path previews, and no exterior wall holes.

## 12. Floor-Mounted Saddles Still Too Awkward

Error:

The floor-mounted serviceable saddles still did not match the desired user sketch/reference. They could remain awkward to thread beside an installed PCB and did not create the clean wall-molded strain-relief language requested.

Fix:

## 13. Long Ladder / Rack Wall Zip-Tie Design

Error:

The wall-integrated zip-tie bridge pass still produced a dense six-per-side ladder/rack/grille visual. It looked like a vented wall panel rather than the individual molded clip shown in the ZIP TIE DESIGN IDEA screenshots.

Fix:

Use the reference folder as source of truth. Default to four individual wall-integrated clips per long wall. Each clip has a compact raised pad, upper rounded slot, lower rounded slot, solid center bridge, and no through-wall cut. Keep the old rack behind `show_old_zip_tie_rack = false` only.

Replace the floor-mounted saddles with internal wall-integrated zip-tie bridge slots. Each feature is a raised/recessed molded pad on the inside wall with an upper slot, a lower slot, and a solid center bridge between them. Slot cuts are limited to the inward pad body so the exterior wall remains solid and sealed.

## 13. Oversized Wall-To-PCB Gap For Zip-Tie Access

Error:

The first wall-integrated zip-tie bridge version solved serviceability but left a large wasted gap between the PCB edge and the inside wall. The side channel looked oversized and not like a compact molded OEM electronics housing.

Fix:

Calculate the side margin from the compact service lane: PCB edge, small clearance, wire lane, small tie clearance, wall-integrated bridge projection, then wall thickness. Keep the wall-integrated bridges, but reduce pad projection and slot size to a compact usable form.

## 14. Preview Geometry Exported Into Production STL

Error:

Preview/helper objects such as PCB placeholders, wire zone markers, wire bundle previews, zip-tie path previews, service clearance markers, and debug helpers were mixed into the same top-level assembly as printable geometry. Exporting without a clean mode separation could include non-printable helper solids in the STL.

Fix:

Add a mode system:

- `mode = "preview"` shows printable enclosure plus helper geometry.
- `mode = "production"` exports only printable enclosure geometry.
- `mode = "cutaway"` is reserved for debug cutaway use.

The SCAD now separates `production_geometry()` from `preview_helpers()`. Preview helpers only render when `is_preview` and their feature toggle are true. Production export was tested to `exports/command_link_rugged_enclosure_production.stl`.

## 15. Wall-Integrated Bridge Slots Still Too Blocky

Error:

The accepted wall-integrated bridge concept still looked too blocky, with crude slot interiors and a repeated hard-rail appearance.

Fix:

Refine `wall_integrated_zip_tie_bridge()` and its cutouts:

- rounded pad perimeter
- wider 7.0 mm slots
- 2.4 mm slot height
- 3.5 mm center bridge
- rounded/chamfered slot mouths
- recessed internal channel behind the center bridge
- individual side blends instead of a continuous rail
- slot cut depth limited to the inward pad so the exterior wall stays solid

## 16. Zip-Tie Mount Audit Needed

Error:

The wall-integrated zip-tie bridge concept was directionally correct, but it still needed a formal count, clearance, serviceability, exterior-wall, slot-smoothness, and export-safety audit. Without that audit, it was too easy to assume the slots were usable just because they looked plausible in preview.

Fix:

Create `ZIP_TIE_MOUNT_AUDIT.md` and audit the current model:

- left long wall: 6 usable bridge features
- right long wall: 6 usable bridge features
- total: 12 bridge features
- slot size: 7.0 mm wide by 2.4 mm high
- nominal preview tie: 4.0 mm wide by 1.4 mm thick
- exterior wall remains solid behind every slot
- production mode exports only printable enclosure geometry
- preview helpers remain guarded by `is_preview`

Also add `show_slot_cutout_preview`, named rounded/chamfered slot cutters, and service-clearance preview helpers so the slot path and wire lane can be reviewed from inside the enclosure.

## 17. Boxy Manufacturing Transitions

Error:

The enclosure still had too many sharp/blocky manufacturing transitions around wall-integrated zip-tie pads, external mount bosses, mount gussets, the grommet boss, rim strips, wire pads, and guide blocks. A first attempt at true repeated 3D chamfering made production export too slow.

Fix:

Apply a focused manufacturing cleanup using fast OpenSCAD-safe geometry:

- add `edge_chamfer`, `large_edge_chamfer`, `rim_chamfer_size`, `slot_edge_chamfer`, `mount_transition_radius`, `boss_blend_radius`, `grommet_boss_blend_radius`, and `molding_draft_angle_preview`
- add named helpers for rounded/chamfer intent: `chamfered_box()`, `rounded_box_approx()`, `soft_edge_pad()`, `molded_pad()`, `boss_blend_pad()`, `rim_chamfer()`, `mount_ear_transition_blend()`, and `grommet_boss_blend()`
- keep zip-tie slot smoothing with rounded/chamfered slot cutters
- use tapered boss blends on external mount bosses
- use cylinder-seeded hulls for cleaner mount gussets
- add a tapered grommet boss wall blend
- document future injection-molding limits in `MANUFACTURING_REVIEW.md`

Production export passed after simplifying the expensive chamfer implementation.

## 18. Ladder Rack Zip-Tie Redesign Rejected

Error:

Even after rounding, the six-per-side wall-integrated zip-tie design still looked like a long ladder/rack/grille and did not match the ZIP TIE DESIGN IDEA reference screenshots.

Fix:

Replace the default with four individual wall-integrated clips per long side:

- `wall_tie_count_per_side = 4`
- `wall_tie_y_positions_4 = [14, 30, 52, 68]`
- `wall_tie_clip_body()`
- `wall_tie_slot_cuts()`
- `wall_tie_clip()`
- `wall_tie_clip_layout()`
- `show_old_zip_tie_rack = false`

Keep optional six-per-side layout as a parameter option only. The reference screenshots and Markdown are now the zip-tie design source of truth.

## 19. Overcomplicated External Mount Ears Rejected

Error:

The external mounting points still looked like stacked cylinders/pads with small arms and decorative gussets. That style did not fit the rugged automotive electronics target and looked weaker than a simple integrated mounting ear.

Fix:

Replace the default external mount path with simple integrated ears:

- `external_mount_style = "simple_integrated_ear"`
- `show_old_external_mounts = false`
- `external_mount_layout()`
- `simple_integrated_mount_ear()`
- 18 mm long x 16 mm wide x 5 mm thick tab
- 4.3 mm screw clearance hole
- 10 mm OD x 1.5 mm high low boss
- two simple side gussets kept clear of screw access

Future rugged enclosure mounts should be wide, simple, rounded, and directly loaded into the enclosure wall/floor before adding any truss or decorative rib geometry.

## 20. No Lid / Seal / Relay Mount Strategy

Error:

The rugged lower enclosure had no matching top half, no O-ring sealing strategy, and no defined way to mount the planned automotive relays.

Fix:

Create a separate `command_link_rugged_lid.scad` file with:

- mode-based preview vs production behavior
- 3.5 mm rugged top panel
- underside sealing lip
- first-pass O-ring groove for a 2.0 mm cross-section O-ring
- six M3 lid screw clearance holes
- five relay mount zones
- ten underside M3 heat-set insert bosses for relay brackets
- underside reinforcement ribs
- preview-only lower base, relay, O-ring, and insert helpers

The lower base was not modified in this pass. A required follow-up is documented in `BASE_UPDATE_REQUIRED_FOR_LID.md` for lower insert bosses and sealing ledge/landing geometry.

## 21. Lid/Base Mating Was Incomplete

Error:

The lid file had an O-ring groove and lid screw clearance holes, but the lower enclosure did not yet have matching base-side seal land geometry or lid-screw heat-set insert bosses. This made the lid concept look complete while the actual base/lid assembly was mechanically incomplete.

Fix:

- Added `command_link_shared_dimensions.scad` for shared seal and fastener dimensions.
- Updated the base with `base_sealing_land()` so the lid O-ring has a defined compression surface.
- Added six blind M3 base insert bosses using `base_lid_insert_boss_layout()`.
- Updated the lid to use the same shared fastener coordinate function.
- Added `BASE_LID_MATING_AUDIT.md` to explicitly mark pass/fail/partial status.

Remaining issue:

The screw holes are inside the compact perimeter seal line. Base insert holes are blind, but final weather sealing still needs sealing washers, thread sealant, or a revised isolated screw-boss strategy.

## 22. Separate Sidewall Lid Post Lane Wasted Width

Error:

The base-side lid insert bosses were added as separate inboard columns while the zip-tie clips stayed on the inside wall. This created a visible wasted side channel and made the enclosure wider than needed.

Fix:

- Changed the shared lid/base fastener side inset from 10.0 mm to 8.0 mm, then to 6.0 mm during the flush wall refactor.
- Added `side_wall_service_spine()` to combine wall, zip-tie clips, and lid insert support into one side-wall system.
- Added `wall_integrated_lid_insert_boss()` and `wall_lid_boss_reinforcement()` so the bosses merge into the wall/spine.
- Reduced side clearance stack from 15.40 mm to 14.25 mm per side.
- Updated the lid through-hole pattern through the shared dimensions file.

Remaining issue:

The compact side zone now shares space between wire routing and lid bosses. Harness routing and zip-tie access must be checked on a physical print with the real PCB and wires.

## 23. Raised Zip-Tie Slot Frames Rejected

Error:

The side-wall zip-tie area still looked wrong because each slot was surrounded by its own raised framed extrusion. The lid insert post areas also interrupted the wall with bulky tower-like geometry. The result was cluttered and not a simple molded wall.

Fix:

- Disabled the default raised `wall_tie_clip_body()` geometry.
- Kept the old raised/pod modules only as non-default legacy code.
- Added `zip_tie_slot_array_cutouts()` so slots are subtractive cuts in the continuous side wall.
- Made `side_wall_service_spine()` a full-height wall band instead of a low rail.
- Tightened the shared lid/base fastener inset to 6.0 mm and reduced the integrated boss OD to 7.0 mm.
- Regenerated the production STL and flat-wall verification renders.

Remaining issue:

The through-wall slot design is visually cleaner and more manufacturable, but actual zip-tie threading, wire capture, and sealing implications must be tested physically.

## 24. Zip-Tie Slot Design Removed

Error:

Multiple iterations of generated zip-tie slots were not acceptable. The feature kept consuming design time and risked reintroducing rejected visual or functional assumptions.

Fix:

- Removed all active zip-tie slot cutouts from the default production geometry.
- Disabled zip-tie clip, bridge, rack, path-preview, cutout-preview, and wire-bundle tie-preview geometry by default.
- Added `show_zip_tie_features = false` as the controlling default.
- Created `ZIP_TIE_REMOVAL_AUDIT.md`.

Rule:

Do not re-add zip-tie slots to the COMMAND LINK lower enclosure unless the user explicitly asks for that geometry. The user will add the slots manually later.

## 25. Grommet Landing Needed Clearance Verification

Error:

The main circular wire-entry hole existed, but the outside boss was only 24.0 mm OD. That left no radial margin for a nominal 24.0 mm waterproof rubber grommet flange and did not make inside/outside clearance visible.

Fix:

- Kept `main_grommet_hole_diameter = 16.0`.
- Added grommet flange and cable gland preview parameters.
- Increased the outside grommet landing to 28.0 mm OD.
- Added 0.8 mm production chamfer cuts at the grommet hole mouths.
- Added preview-only outside flange, inside flange, wall grip, centerline, optional cable gland nut, and wire bend clearance helpers.
- Created `GROMMET_CLEARANCE_AUDIT.md`.

Remaining issue:

The 20.0 mm wall height is tight for a 24.0 mm inner flange, so the selected real grommet/gland must be physically test fitted.
## 26. Base/Lid Mating Needed Explicit Verification

Problem:
- The lid and base had separate production files, so visual confidence in the
  standalone renders did not prove the parts actually seated, sealed, or aligned.

Fix:
- Added `command_link_base_lid_fit_check.scad`.
- Exported fresh production STLs for both base and lid.
- Imported both STLs into one verification scene with closed, exploded,
  cutaway, O-ring alignment, fastener alignment, and insert-boss views.
- Moved more mating constants into `command_link_shared_dimensions.scad` so the
  base and lid share the same body dimensions, seal values, and fastener layout.

Current result:
- Lid seating, seal-land/groove alignment, and lid screw/base insert alignment
  pass the CAD check.
- O-ring compression, screw sealing, heat-set insert fit, and populated-PCB
  clearance under lid relay bosses still require physical validation.

## 27. Relay Mount Zones Did Not Include Actual Brackets

Problem:
- The lid had relay insert bosses and relay placeholders, but no separate
  printable clamp/retainer pieces.

Fix:
- Added `command_link_relay_brackets.scad` for removable relay retainer
  brackets.
- Added `command_link_relay_layout_dimensions.scad` so the lid insert bosses
  and bracket screw holes share the same relay positions.
- Added preview renders and production STL exports for a single bracket and a
  set of five.

Remaining risk:
- Relay/socket dimensions are assumptions. The bracket capture height and lip
  must be adjusted after measuring the actual relay or socket.

## 28. Grommet Hole Lacked Inside Collar Clearance

Problem:
- The main 16.0 mm wire-entry hole existed, but the inside grommet collar
  envelope overlapped internal wire landing / rail / rib geometry behind the
  front wall.
- Hole diameter alone did not prove a waterproof grommet or gland could seat.

Fix:
- Added a local inside collar relief centered on the grommet hole.
- Added `inside_grommet_clearance_diameter = 28.0`.
- Added `inside_grommet_clearance_depth = 5.0`.
- Added production cut modules `grommet_inner_collar_clearance_cut()` and
  `grommet_inner_landing_relief()`.
- Added preview helper `grommet_inner_clearance_relief_preview()`.

Result:
- Internal rail/ledge interference is removed in CAD while keeping the exterior
  wall closed and preserving the top sealing land.
- Actual grommet or cable gland must still be physically test-fitted.

## 29. Lid Seal Keepout and Relay Clamp Geometry Were Wrong

Problem:
- Lid underside relay/rib features were allowed near the O-ring groove and
  seal channel.
- The fit check did not prove the underside features stayed out of the
  base-wall seating and seal keepout zones.
- The relay bracket still had a bottom/base spine, making it behave like a
  tray rather than a top retainer.

Fix:
- Added hard shared seal keepout parameters.
- Added lid underside no-go cut geometry so relay bosses and ribs are clipped
  away from the O-ring/seal path.
- Changed the relay layout to a compact 3+2 column layout to pull relay insert
  holes away from the perimeter seal.
- Updated the fit-check SCAD with `seal_keepout`, `relay_keepout`, and
  `underside` modes.
- Rebuilt the relay bracket as an open-bottom top retainer with two screw
  feet and no center bottom floor.

Remaining risk:
- Five assumed 28 mm relay bodies are very tight in the current lid footprint.
  The actual relay/socket must be measured before marking the relay layout
  production-ready.

## 30. Cable Gland Hole Lacked Inner Nut / Tool Clearance

Problem:
- The main 16.0 mm wire-entry hole and outside boss existed, but the inside
  relief was sized only for a 28.0 mm rubber grommet flange.
- A waterproof cable gland retaining/compression nut needs more space to sit
  flat and rotate for tightening.
- The internal wire landing / rail / guard directly behind the hole blocked
  the retaining nut and tool/finger clearance envelope.

Fix:
- Added cable-gland-specific parameters with a 28.0 mm inner nut and 34.0 mm
  tool clearance envelope.
- Increased the production inside relief to `inside_fitting_clearance_diameter
  = 34.0` and `inside_fitting_clearance_depth = 8.0`.
- Added `internal_rail_gland_relief_notch()` to remove the local rail/ledge
  obstruction around the fitting.
- Expanded preview helpers to show the threaded body, outside flange, inside
  nut, tool clearance, and wire bend envelope.

Remaining risk:
- The compact 20.0 mm wall height still requires physical test fitting with
  the selected gland or grommet. Nut shape and wrench clearance vary by part.
