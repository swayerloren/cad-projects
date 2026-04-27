# Design Decisions

## Reference-Based Zip-Tie Clip Redesign

- Reject the long ladder/rack/grille wall-tie appearance.
- Use `ZIP TIE DESIGN IDEA/wall-integrated zip-tie bridge slot.MD` and the screenshots as the zip-tie design source of truth.
- Default to four individual wall-integrated clips per long side.
- Keep optional six-per-side spacing available only as a parameter option.
- Keep exterior wall solid; slot cuts are subtracted only from the raised internal clip body.
- Use preview helpers for zip-tie path and wire bundle only in preview mode.

- The design is not just a PCB plate; it is a rugged electronics lower enclosure.
- One circular grommet hole is preferred for all wires.
- The circular grommet hole belongs on a short side of the enclosure.
- Zip tie strain relief should be internal-only.
- Zip tie slots must not cut through exterior walls.
- Zip tie strain relief should look like molded wall-integrated cable-tie bridge slots, not random blocks, towers, or floor saddles trapped beside the PCB.
- Internal wire strain relief should use inside-wall bridge pads with an upper slot, a lower slot, and a solid center bridge for the tie to wrap around.
- The active wire-retention design uses six wall-integrated zip-tie bridges per PCB long side, for twelve total retention points.
- Each wall bridge must be visible and serviceable from inside the enclosure after PCB installation and soldering.
- Wall bridge slot cutouts must be limited to the inward pad body; they must not cut into or through the exterior wall.
- Preview helpers should show the tie path through the upper/lower slots and the wire bundle near the inside wall.
- Wall-integrated tie serviceability should not be achieved by making the enclosure overly wide.
- The current side layout should be compact: PCB edge, 2.5 mm clearance, 6.0 mm wire lane, small tie clearance, wall-integrated bridge pad, exterior wall.
- Side margins should be calculated from the compact service-lane stack when possible, not hard-coded to oversized empty gaps.
- External mounting points must be outside the enclosure body.
- Mount points need truss/rib/gusset support for off-road use.
- Mounting loads should flow into the enclosure wall and floor.
- External mounts should look like clean rounded automotive mounting ears, not rough truss pods.
- External mount ears should use refined oval/teardrop-style lugs, raised screw bosses, wide root necks, and a small number of clean gussets.
- Use only enough gusseting and ribbing to create a clear load path while preserving an OEM-like molded appearance.
- Industrial-design refinements should improve wall continuity, rim appearance, corner softness, and feature consistency without changing PCB mounting geometry.
- Styling should come from molded transitions and consistent radii, not ornamental ribs or decorative detail.
- The main SCAD file should stay consolidated around accepted modules only: circular short-side grommet, internal cable-tie saddles, rounded external ears, real PCB standoffs, board guides, rugged lower body, and preview helpers.
- Dead wrappers, old rejected geometry, and unused parameters should be removed instead of kept for compatibility.
- Strength should come from geometry, not only thickness.
- The PCB must remain installable and removable.
- Solder pad access must remain clear.
- The exterior wall should remain solid except for the intentional grommet/cable-gland hole.
- Future relay board support should remain parameterized and disabled until the relay PCB is finished.
- The rugged enclosure SCAD must use mode-based separation: preview helpers are not production geometry.
- Production STL export must use `mode="production"` and include only printable enclosure solids.
- Preview mode may show PCB placeholder, wire zone markers, zip-tie path previews, wire bundle previews, and clearance markers.
- Wall-integrated zip-tie bridges should read as individual molded recessed service features, not one continuous hard rail.
- The refined wall bridge uses upper/lower rounded service slots with a smooth center bridge and limited-depth cuts that do not enter the exterior wall.
- A formal zip-tie mount audit is required after changing wall-integrated bridge geometry.
- The accepted current bridge count is six per long side, twelve total.
- The accepted current slot size is 7.0 mm wide by 2.4 mm high for a nominal 4.0 mm by 1.4 mm small zip tie.
- The side service lane is intentionally compact, but it must be validated with preview helpers and later with a physical print.
- Slot-mouth smoothing should use rounded/chamfered cutters where practical so the tie does not catch on sharp rectangular edges.
- `show_slot_cutout_preview`, zip-tie path preview, wire bundle preview, and service-clearance preview should be used together before treating the bridge layout as acceptable.
- Manufacturing cleanup should improve transitions without changing the confirmed PCB mounting coordinates, circular grommet hole, twelve wall-integrated zip-tie bridges, or external mounting ear locations.
- Prefer fast OpenSCAD-safe rounded/chamfered approximations over repeated expensive `minkowski()`, `offset()`, or nested `hull()` operations that make production export unreliable.
- External mount bosses should use tapered boss blends and rounded gusset ends instead of abrupt cylinders and square rib ends.
- The grommet boss should use a tapered circular wall blend while preserving the 16.0 mm circular hole.
- The current design remains FDM-first; injection molding awareness is documented, but final molding would require draft, coring, parting-line, and side-action review.
- The accepted external mounting target is now simple integrated ears, not layered pods or trussed mount stacks.
- External mounts should use a wide tab/neck, one screw hole, one low boss, and simple side gussets that stay clear of the screw and washer path.
- The old external mount layout must stay disabled by default with `show_old_external_mounts = false`.
- A separate rugged top lid file has been started: `command_link_rugged_lid.scad`.
- The lid is not a flat plate; it carries five automotive relay bracket mount zones on underside heat-set insert bosses.
- The lid uses a first-pass underside O-ring groove and downward sealing/alignment lip.
- The lid has six M3 clearance holes intended to fasten into future heat-set insert bosses in the lower base.
- The lower base must get matching lid insert bosses and a base-side seal landing in a later pass before the enclosure is mechanically complete.
- Five 28 mm relay placeholders do not fit in one row on the compact lid, so the lid automatically falls back to a staggered 3+2 relay layout.

## Base/Lid Mating Update - 2026-04-26

- A lid-only O-ring groove is not sufficient unless the lower base has a matching sealing land.
- The lower enclosure now includes a production `base_sealing_land()` around the top perimeter.
- The lower enclosure now includes six blind M3 heat-set insert bosses for lid screws.
- The lid and base now share `command_link_lid_fastener_positions()` through `command_link_shared_dimensions.scad`.
- The shared lid fastener edge offset was initially 10.0 mm, then compacted to 8.0 mm so the insert bosses merge into the side-wall service spine.
- Relay bracket inserts on the lid remain separate from lid-to-base fasteners.
- The compact design keeps lid screws inside the seal line; final weather sealing may need sealing washers, thread sealant, or a revised screw-isolation detail.

## Sidewall Compaction Update - 2026-04-26

- A separate inboard lid mounting post lane was rejected.
- The lower enclosure now uses an integrated side-wall service spine.
- Lid insert bosses should merge into the side wall/spine instead of standing alone as separate tall cylinders.
- Zip-tie clips and lid screw bosses should align on the same long-wall service system.
- Shared lid/base fastener side inset changed from 10.0 mm to 8.0 mm, then to 6.0 mm for the flush wall refactor.
- Side margin changed from 15.40 mm per side to 14.25 mm per side, reducing body width from 95.80 mm to 93.50 mm.
- Zip-tie clip projection changed to 2.5 mm and default clip positions changed to `[14, 30, 52, 68]` to avoid crowding the middle lid boss.

## Flush Zip-Tie Wall Refactor - 2026-04-26

- Raised slot frames/pods around individual zip-tie slots were rejected.
- The accepted direction is a flat continuous side-wall band with zip-tie slots cut through it.
- The wall should stay visually flush around integrated lid insert holes.
- Robust enclosure design does not require cluttered local extrusions around every functional slot.
- Shared lid/base fastener side inset changed to 6.0 mm so insert holes sit inside the clean wall band.
- Side-wall insert boss OD changed to 7.0 mm to fit the flatter wall architecture.

## Zip-Tie Slots Removed From Active Model - 2026-04-26

- All zip-tie slot geometry is removed from the active lower enclosure default.
- The user will add the final zip-tie slots manually later.
- `show_zip_tie_features = false` is now the controlling default.
- Do not re-add zip-tie slots, bridge pads, rack holes, or tie path previews unless explicitly requested.
- Preserve the solid side walls, base sealing land, lid insert bosses, PCB standoffs, grommet hole, and external mounting ears while the manual slot design is pending.

## Grommet Clearance Update - 2026-04-26

- Main wire entry remains a 16.0 mm circular front short-wall hole.
- Outside grommet landing boss is now sized for a 24.0 mm rubber grommet flange plus 2.0 mm radial margin, so the boss OD is 28.0 mm.
- Hole-mouth chamfers are production geometry to reduce sharp edges against rubber.
- Grommet flange, wall grip, optional gland nut, and wire bend radius are preview-only helpers and must not export in production mode.
- A real grommet or cable gland must be physically tested because a 24.0 mm inner flange is tight against the 20.0 mm wall height.
## Base/Lid Fit Verification - 2026-04-26

- Created `command_link_base_lid_fit_check.scad` as the assembly verification scene for the lower base and relay lid.
- Base and lid must continue to use `command_link_shared_dimensions.scad` for seal dimensions and lid fastener positions.
- The lid O-ring groove remains on the lid underside; the lower base owns the raised sealing land.
- The six lid screw clearance holes align to the six blind base heat-set insert pilot holes through the shared fastener layout.
- The current compact design keeps lid screws inside the seal line; final weatherproofing may need sealing washers, thread sealing, or isolated screw details.
- Do not reintroduce zip-tie slots while working on base/lid mating.

## Relay Bracket Parts - 2026-04-26

- Added separate removable relay retainer brackets in `command_link_relay_brackets.scad`.
- Lid production STL must not include bracket solids. The lid only owns heat-set insert bosses/pilot holes and a preview overlay.
- Relay layout and bracket screw positions are shared through `command_link_relay_layout_dimensions.scad`.
- The requested single row of five 28 mm relays does not fit the compact lid, so the resolved active layout is staggered 3+2.
- Current bracket concept is a two-screw retainer strap with a raised bridge and capture lip, not a permanent relay cage.
- Relay/socket dimensions are assumptions until the actual relay or socket is measured.

## Grommet Inside Collar Relief - 2026-04-26

- The main wire-entry hole must be checked as a full grommet/gland envelope, not only a circular wall cut.
- The accepted lower enclosure now includes a local inside relief zone for the grommet collar.
- The inside relief is 28.0 mm diameter x 5.0 mm deep from the inside wall face.
- The relief removes local internal rail/ledge interference while preserving the exterior wall and top sealing land.
- Do not add internal wire rails or ribs back into the grommet collar envelope.
- Final waterproofing still depends on physical fit with the selected grommet/gland.

## Lid Seal Keepout and Open Relay Clamp - 2026-04-27

- Lid underside geometry must obey a hard perimeter seal keepout.
- Relay bosses, relay ribs, relay bracket previews, and relay placeholders must
  not cross the actual O-ring groove/channel.
- The base/lid fit must be checked in a dedicated fit-check scene after fresh
  production STL export.
- Relay retainer brackets must be open-bottom top retainers, not trays.
- A compact 3+2 relay column layout is now preferred over the failed single-row
  and wide staggered patterns for the current lid footprint.
- The relay layout remains conditional on measuring the actual relay/socket.

## Cable Gland Inner Nut Clearance - 2026-04-27

- The main wire-entry feature must support both rubber grommets and waterproof
  cable glands.
- A wall hole plus outside boss is not enough; the inside retaining nut and
  tightening tool envelope must be modeled.
- The active lower enclosure uses `main_wire_entry_type = "cable_gland"` and a
  34.0 mm inside fitting/tool clearance envelope.
- Internal rails, ledges, and wire guards must be locally relieved around the
  gland so the nut can seat and rotate.
- Do not add wire-routing ribs back into the cable-gland nut clearance zone.
