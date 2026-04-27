# Manufacturing Notes

## 3D Printing

- Prefer PETG, ASA, ABS, nylon, PA-CF, or another tough material suited to heat, vibration, and outdoor exposure.
- PLA is not preferred for UTV heat/vibration environments.
- Orient the print so external mount pods, standoffs, and wall features have favorable layer direction for expected loads.
- Avoid thin unsupported tabs.
- Avoid tall unbraced posts.
- Use enough perimeters around bosses, standoffs, and mount pods.
- Keep molded style features shallow and printable: small rim caps, stepped bosses, and softened edges should not create fragile overhangs.
- Consider printing a small coupon for heat-set insert fit before printing the full part.

## Heat-Set Inserts

- Default insert pilot is `insert_hole_diameter = 4.2`.
- Default insert depth is `insert_depth = 5.0`.
- Verify these values against the actual M3 heat-set inserts.
- Install inserts with controlled heat and alignment.
- Avoid overheating the boss.
- Use reinforced standoff bases and gussets around insert bosses.

## Grommet / Cable Gland

- Current wire entry is one circular short-side hole.
- Default hole diameter is `main_grommet_hole_diameter = 16.0`.
- Outside grommet landing boss is now 28.0 mm OD for a 24.0 mm flange plus 2.0 mm radial margin.
- Grommet hole-mouth chamfer is `grommet_hole_edge_chamfer = 0.8`.
- Preview helpers show outside/inside flanges, wall grip zone, optional gland nut, and wire bend envelope.
- Verify the rubber grommet or cable gland before final print.
- Keep the grommet boss/ring if it helps support compression or sealing.
- A 24.0 mm inner flange is tight against the 20.0 mm wall height; physical fit is mandatory.
- Do not add random wall gaps for wires.

## Off-Road Vibration

- Mount pods should have thick bosses, triangular gussets, diagonal ribs, and load paths into the enclosure wall/floor.
- PCB standoffs should be reinforced and should not act as isolated posts.
- Wire strain relief must reduce fatigue at solder joints.
- Fasteners may need washers, threadlocker, or vibration-resistant hardware depending on final assembly.

## Leak Path Awareness

- Zip-tie anchors must be internal-only.
- Do not cut zip-tie slots through the exterior wall.
- Keep exterior walls solid except for the intentional grommet/cable-gland hole.

## Injection Molding Future Considerations

- Avoid unnecessary thick solid masses.
- Convert heavy sections into ribs and supported bosses where possible.
- Watch for sink around mount bosses and standoff bosses.
- Current rounded shell, top rim, and stepped grommet boss are style/prototype approximations; true injection molding would still need draft and wall-thickness review.
- Add draft and more molding-specific details only if the design moves toward injection molding.
- The circular grommet hole is a side feature and would likely need a side core or redesigned tooling strategy.
- The internal wall-integrated zip-tie bridge slots are good for FDM serviceability but may require side actions or redesign for straight-pull molding.
- External mount bosses now use tapered blends, but a molded version still needs boss coring and sink review.
- Use fast rounded/chamfered OpenSCAD approximations for prototype cleanup; avoid render-heavy fillet methods unless the part still exports reliably.

## Serviceability

- Preserve PCB installation/removal.
- Preserve screwdriver access to PCB screws.
- Preserve solder pad access.
- Preserve room for wire bend radius and zip tie installation.

## Latest Manufacturing Cleanup Pass

- Added `MANUFACTURING_REVIEW.md` in the project source folder.
- Added manufacturing parameters for edge softening, rim softening, mount transitions, boss blends, grommet boss blend, and molding draft review.
- Refined zip-tie slot entries, wall-tie pads, external mount boss blends, mount gusset end shape, mount root transitions, and grommet boss wall blend.
- Production export passed after avoiding slow repeated true-fillet approximations.
- Remaining validation: printed coupons for manual zip-tie slots, grommet, heat-set inserts, and external mount fastener load.

## External Mount Redesign Update

- The stacked/layered external mount style was rejected after visual review.
- Active target is simple integrated automotive/electronics-module mounting ears.
- Use a wide 16 mm tab/neck, 5 mm tab thickness, one 4.3 mm clearance hole, and one low 10 mm x 1.5 mm boss.
- Use simple side gussets, not decorative truss clutter.
- Keep screw/washer access clear; do not run a central rib through the screw boss.
- Production STL exported after the redesign, but real off-road durability still needs print and vibration/fastener testing.

## Rugged Relay Lid Manufacturing Notes

- New lid file: `command_link_rugged_lid.scad`.
- The lid is FDM-first but designed with future molding awareness.
- Print orientation should be evaluated two ways: outside face down for best exterior finish, or underside up for easier relay-boss/insert-hole quality.
- Relay bracket insert bosses are blind underside bosses; actual insert pilot/depth must be tested with the chosen M3 inserts.
- The O-ring groove is first-pass geometry for a 2.0 mm cross-section O-ring and must be validated with actual O-ring material and screw clamp load.
- The lid screw holes currently require matching lower-base insert bosses in a future base update.
- Lid screw holes may become leak paths unless isolated with boss geometry, gasket washers, or a revised seal path.
- Future injection molding requires draft, boss coring, rib thickness review, and a defined parting line.

## Base/Lid Seal And Insert Manufacturing Update

- The lower base now has a raised sealing land that mates to the lid underside O-ring groove.
- The lower base now has six blind M3 heat-set insert bosses for lid screws.
- Base and lid fastener positions come from `command_link_shared_dimensions.scad` to avoid coordinate drift.
- The base insert holes are blind, which prevents a direct through-base leak path.
- Lid screw holes remain inside the seal line, so final weatherproofing should use sealing washers, thread sealant, or a revised isolated screw-boss strategy.
- Print validation is required for O-ring compression, heat-set insert pilot fit, and screw clamp load before treating the enclosure as sealed.

## Sidewall Service Spine Manufacturing Update

- The lower base now integrates lid insert bosses into the side-wall service spine instead of using separate inboard columns.
- The side spine ties lid insert bosses, zip-tie clips, and wall reinforcement into one molded side-zone system.
- Body width was reduced from 95.80 mm to 93.50 mm by removing the separate post lane.
- The integrated bosses are more compact but create local interruptions in the wire lane; harness fit must be checked with the real wire bundle.
- Future molding review should check rib thickness, boss coring, and tool access around the full-height wall/boss webs.

## Flush Zip-Tie Wall Manufacturing Update

- Raised slot frames were removed from the accepted default geometry.
- Zip-tie openings are now clean rounded cutouts through a continuous flat side-wall band.
- The insert post areas are integrated into the same flat wall band rather than added as bulky standalone towers.
- This is cleaner for FDM surface quality and closer to a controlled molded enclosure wall.
- The through-wall zip-tie slots must be checked against final environmental sealing expectations.
## Base/Lid Fit And Seal Verification - 2026-04-26

- Base/lid assembly is now checked in `command_link_base_lid_fit_check.scad`
  using fresh production STL imports.
- The O-ring groove is on the lid underside and aligns over the raised base
  sealing land.
- CAD check confirms shared screw axes pass through the lid clearance holes and
  base blind insert pilot holes.
- The current compact screw layout places screws inside the seal line. For real
  weatherproof use, plan sealing washers, thread sealant, or isolated screw
  towers.
- O-ring compression is a first-pass CAD target only. Real O-ring material,
  durometer, groove fill, compression force, and printed tolerance must be
  tested.
- Relay bracket insert bosses on the lid underside are close to the generic PCB
  component envelope; validate against the populated board before printing a
  final lid.

## Relay Retainer Brackets - 2026-04-26

- Brackets are separate serviceable parts, not part of the lid production STL.
- Prototype bracket material should be PETG minimum; ASA/ABS or nylon/fiber
  nylon is preferred for heat and vibration. Do not use PLA for final UTV use.
- The current printed bracket is a two-screw retainer strap with a raised
  bridge and capture lip. It is simple and serviceable, but actual relay/socket
  retention must be vibration tested.
- A metal strap may be better long term if temperature or clamp load makes a
  printed retainer unreliable.
- M3 screw head clearance and heat-set insert pilot dimensions must be matched
  to actual hardware.

## Grommet Inner Collar Relief - 2026-04-26

- The 16.0 mm wall hole now has a local 28.0 mm inside clearance relief for the
  grommet/gland collar.
- The relief removes low internal rail/rib geometry that blocked the inside
  collar from seating.
- The relief starts at the inside wall face and does not cut through the
  exterior wall.
- Because the enclosure wall height is compact, the selected real grommet or
  gland must still be checked for flange height, panel grip range, and bend
  clearance.

## Lid Seal Keepout / Relay Retainers - 2026-04-27

- Treat the O-ring groove and base-wall seating region as hard no-go geometry.
  Do not add underside ribs, bosses, clamp feet, or preview solids across the
  seal channel.
- The lid now clips underside relay bosses and ribs away from the seal keepout
  using production geometry logic, not just preview coloring.
- Relay retainer brackets should be simple open-bottom top bridges with screw
  feet. Do not use bottom tray floors under relay/socket bodies.
- The compact five-relay layout is still dependent on actual relay/socket
  dimensions. Measure hardware before printing a production lid.
- Printed relay brackets need heat and vibration testing; ASA/ABS or nylon is
  preferred over PLA.

## Cable Gland Install Clearance - 2026-04-27

- Cable gland installation requires room for the inside retaining nut and tool
  access, not just the gland thread hole.
- The lower enclosure now includes a 34.0 mm inside clearance envelope and
  local rail/ledge relief behind the wire-entry hole.
- Preview mode shows the gland thread, outside flange, inside nut, tool
  clearance, and wire bend path.
- Production mode exports only the enclosure relief and hole/boss geometry.
- The selected gland must still be test-fitted because across-flats nut size,
  wrench shape, and thread length vary.
