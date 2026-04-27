# Errors And Fixes

## OpenSCAD CLI string selector issue

Problem: PowerShell command-line rendering with `preview_part="base_plate"` caused OpenSCAD to interpret `base_plate` as an unknown variable, producing empty individual exports.

Fix: Added numeric `preview_id` selector:

- 0 assembly
- 1 base plate
- 2 top plate
- 3 ring gear
- 4 drive gear
- 5 driven gear
- 6 connecting gear
- 7 gear block
- 8 crank
- 9 handle
- 10 crank stop
- 11 tape arm
- 12 tape roller
- 13 tape roller stop

## Initial dimensional mismatches

Problem: Handle was too narrow, tape arm boss was too small, and plate/ring outlines were slightly oversize.

Fix: Adjusted handle envelope, tape arm lobe, plate X scale, and ring X scale. Re-exported STLs and comparison screenshots.

## Mechanically wrong gear assembly

Problem: The rebuild matched many bounding boxes but the assembly was mechanically wrong. Connecting gears were placed on separate inferred centers, the drive/driven/ring gear relationships did not use pitch-circle center distances, and the preview looked randomly stacked.

Fix: Rebuilt the assembly as a two-plane gear train:

- lower plane: ring gear plus two small connecting gears
- upper plane: drive gear plus two driven gears
- shared axes: each driven gear shares an axis with a connecting gear
- drive gear center: placed at the pitch-distance intersection of the two driven gears
- ring gear center: fit to the two connecting gear axes and ring pitch assumption

Added `MECHANICAL_ACCURACY_REVIEW.md`, pitch-circle previews, axis-line debug helpers, cable path preview, and improved root/pitch/tip tooth profiles.

Rule for future gear rebuilds: never accept a gear mechanism from bounding boxes alone. Compare tooth count, pitch circle, center distance, shared shafts, stack order, and functional motion path.
