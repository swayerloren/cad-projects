# Changelog

## 2026-04-25

- Reduced the wall-integrated zip-tie side gap by replacing the fixed 26 mm side margins with a computed compact service-lane margin.
- Added compact service-lane parameters for PCB clearance, wire lane width, tie clearance, wall-tie projection, and subtle wall-tie strip blending.
- Preserved six wall-integrated tie bridges per long side and kept the exterior wall solid.

## 2026-04-25

- Replaced the latest floor-mounted zip-tie saddle concept with internal wall-integrated zip-tie bridge slots.
- Added six wall-integrated bridge slots per long side, twelve total, using upper/lower inside-facing slots and a solid center bridge.
- Kept slot cutouts limited to the inward pad body so the exterior wall remains solid.
- Updated wire-retention preview direction to show the internal tie path and nearby wire bundle.

## 2026-04-25

- Initial PCB mechanical analysis completed.
- Confirmed PCB dimensions, mounting holes, solder pad zones, and tallest component.
- First internal PCB carrier tray concept created.
- First carrier was judged too weak and lacked protective walls.
- Rugged lower enclosure concept added.
- Rectangular side wire opening was rejected.
- Zip-tie holes through the wall were rejected.
- Circular short-side grommet hole required for all external wires.
- Standalone and through-wall zip-tie features replaced with internal-only anchors.
- Internal wire strain relief refined into low-profile wall-side wire lanes with bridge-style cable-tie saddles and pass-under tie tunnels.
- Outside flat mounting tabs rejected as too weak.
- Reinforced truss/gusset mount pods required for off-road vibration and shock.
- Rough external mount pods were replaced with refined rounded OEM-style ears using oval/teardrop lugs, raised bosses, wider necks, and two clean gussets per ear.
- Industrial-design refinement pass added a continuous rounded wall shell, small molded top rim, stepped grommet boss, and consistent softened feature radii without moving PCB or wire-retention features.
- Final SCAD consolidation pass organized parameters and modules by function, removed unused/rejected wrappers and parameters, and kept only the accepted grommet, wire-retention, standoff, enclosure body, and external mount architecture.
- Replaced the unusable three-saddle wire-retention geometry with twelve real internal cable-tie bridge tunnels: six per long PCB side, with visible zip-tie path previews and solid exterior walls.
- Replaced the trapped side-channel bridge geometry with open-top serviceable cable-tie saddles, wider side margins, wire-bundle previews, and service-clearance previews for after-PCB-install zip-tie threading.
- Current rugged enclosure keeps the future relay board placeholders disabled until the relay PCB is known.
