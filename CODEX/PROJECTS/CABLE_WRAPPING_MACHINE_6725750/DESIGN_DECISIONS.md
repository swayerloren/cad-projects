# Design Decisions

- Rebuilt geometry as parametric primitives and 2D profiles, not raw mesh conversion.
- Used original STLs only for measurements and optional translucent overlays.
- Used a new clean assembly coordinate system instead of source print-bed coordinates.
- Added both string `preview_part` and numeric `preview_id` selectors for easier scripted rendering on Windows.
- Modeled gears with simplified trapezoidal teeth, preserving measured OD/root/bore/height/tooth-count parameters.
- Modeled ring gear as an arc band with outer teeth and a measured D12 pin.
- Documented assembly placement as inferred because no original assembled CAD file was available.
- Kept serviceability notes explicit because the source README says the model is glued.

## Correction pass decisions - 2026-04-26

- Treated the original as a two-plane gear mechanism rather than a single random gear layer.
- Used measured plate shaft holes as the shared axes for driven and connecting gears.
- Moved the drive gear to a pitch-distance solution that meshes with both driven gears.
- Used a 116 mm inferred ring pitch diameter so the ring can mesh with the connecting gear axes.
- Increased ring arc teeth to 52 and changed all gears to root/pitch/tip tooth polygons.
- Added preview helpers for pitch circles, axis lines, original overlays, exploded view, part labels, and cable/tape path.
- Documented that the exact ring pitch, backlash, tape arm angle, and glue clearances remain assumptions without original assembled CAD.
