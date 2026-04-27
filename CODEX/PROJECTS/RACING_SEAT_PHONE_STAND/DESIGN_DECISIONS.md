# Design Decisions

- Rebuilt as three editable modules: seat shell, base, rollcage.
- Used measured STL bounding boxes as primary dimensions.
- Modeled phone support explicitly with slot, lip, cable cutout, and backrest angle.
- Used `tube_between()` cylinders for rollcage and bolsters instead of expensive sphere hulls.
- Made base slightly thicker than source for printable stiffness.
- Kept STL imports as translucent overlays only.
- Used `openscad.com` for reliable Windows command-line rendering.

## Refinement Pass Decisions

- Rejected the previous envelope-only rebuild quality.
- Added visual accuracy review before claiming the rebuild is acceptable.
- Added a real phone placeholder to validate stand function.
- Revised the seat to emphasize bucket-seat silhouette, side bolsters, raised cushion pads, harness slots, cable cutout, front lip, and phone slot.
- Revised the base to include wider rail footprint, rounded pads, truss webbing, holes, and text approximation.
- Revised the rollcage into a structured hoop/side-frame/truss assembly using named tube segment modules.
- Added comparison controls: `show_original_overlay`, `show_comparison_planes`, `show_cutaway`, `show_part_labels`, and `comparison_preview()`.

## V2 Rebuild Decisions

- Use the `pre made traiing models 3d\racing seat phone stand` folder as the current source because the separate older folder was not present.
- Create V2 in a new `openscad_rebuild_v2` folder instead of modifying the prior rebuild.
- Treat the product as a styled functional object, not only as three STL envelopes.
- Use preview colors that match the reference identity: red seat shell, black cushion/roll cage/truss, gray rails.
- Model the roll cage with `tube_between_points()` cylinder segments only; do not use flat bars or random lines.
- Model the base as side rails plus truss webbing and screw/bolt boss pads, not a plain rectangle.
- Keep the phone placeholder preview-only and use it to verify front lip/backrest function.
- Keep original STL overlays preview-only and production exports as rebuild geometry only.
- Accept that exact organic seat curvature is simplified; prioritize silhouette, openings, bolsters, and phone-cradle function.

## Photo Review Decisions - 2026-04-26

- Treat the three decoded JPEG reference photos as primary visual evidence for V2 refinement.
- Keep the red seat, black cushion/cage/truss, and gray rail color separation because the photos show product variants with that same part-language.
- Increase the V2 backrest angle to better match the side-view photo.
- Increase the phone placeholder lean angle so the functional cradle reads clearly in render checks.
- Bias roll cage diagonal braces to the side/rear frame so they match the photographed tube structure instead of crossing the main phone face.
- Keep the rail/truss base approach; exact decorative side-plate cutouts remain future refinement.

## V3 Decisions

- Do not keep patching V2 after it failed the reference-photo check.
- Create `openscad_rebuild_v3` as a clean versioned rebuild.
- Separate V3 into five systems: seat shell, side rail/truss base, roll cage tube frame, phone placeholder, and reference overlay.
- Use layered hull profiles for the seat shell rather than V2's simpler slab/profile structure.
- Use side rails with rounded screw tabs and boss rings so rail hardware is visually obvious.
- Use triangular side truss ribs to make the side silhouette closer to the photos.
- Use production mode with lower tube resolution and no tube end spheres so STL export completes.
- Mark V3 quality honestly as improved but still rough.
