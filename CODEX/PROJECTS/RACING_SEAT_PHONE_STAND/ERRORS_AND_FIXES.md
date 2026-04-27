# Errors And Fixes

## OpenSCAD executable behavior

Problem: `openscad.exe` returned without producing useful CLI diagnostics or output files for this model.

Fix: Switched scripted renders to `openscad.com`, which generated proper diagnostics and files.

## Slow CGAL export

Problem: Initial tube implementation used hulls of spheres, making exports too slow.

Fix: Replaced tube hulls with vector-aligned cylinders in `tube_between()`.

## Envelope mismatch

Problem: Initial rebuild seat depth was too shallow and base width too narrow.

Fix: Added `backrest_y_offset`, widened `base_rail_sep`, and reduced rollcage height so final envelopes matched closely.

## Visual accuracy failure

Problem: The previous rebuild matched bounding boxes but failed visual/style/function accuracy. The seat looked like a flat board, the rollcage looked like crude random lines, the base was too simple, and the phone stand function was not validated.

Fix: Added `VISUAL_ACCURACY_REVIEW.md`, refined the seat pan/backrest/bolsters/base/rollcage, added original overlay and side-by-side comparison tooling, and added a phone placeholder fit check.

Rule: Future STL rebuilds must review silhouette, style, and function explicitly, not just bounding boxes.

## V2 rebuild required after refinement still missed identity

Problem: The earlier refinement was still not acceptable because it did not fully capture the reference product identity: red racing bucket seat, gray/black rail base, black tube roll cage, side triangular truss supports, screw/bolt points, front phone catch, and functional phone cradle behavior.

Fix: Create a new clean V2 rebuild in:

```text
C:\Users\LJ\OpenSCAD Projects\pre made traiing models 3d\racing seat phone stand\openscad_rebuild_v2
```

V2 explicitly models:

- racing bucket seat silhouette
- head/shoulder harness openings
- lower harness/pass-through opening
- front phone lip and phone slot support
- phone placeholder and side-view fit check
- gray side rails with screw holes and boss pads
- black triangular truss webbing
- black roll cage as real tube segments
- rear hoop, lower frame, diagonal braces, and attachment blocks

Rule: Styled product rebuilds must preserve product identity, part color separation, major visual openings, and functional placeholder checks before being considered acceptable.

## Reference Photos Added After V2

Issue: Reference photos were added after the initial V2 rebuild. A styled product rebuild can still be wrong if it is not checked against photos, even when it includes the right named modules and STL-sized parts.

Fix:

- Created `REFERENCE_PHOTO_REVIEW.md`.
- Reviewed the three decodable JPEG photos and explicitly marked the AVIF as not locally decoded.
- Updated V2 parameters for backrest lean and phone lean.
- Adjusted roll cage bracing to side/rear structure based on the side photo.
- Generated photo-review assembly, front, side, and phone-fit renders.

Rule: When photos exist, they must guide styled-product rebuild acceptance. Bounding boxes and STL envelopes are not enough.

## V2 Still Failed Against Photos

Issue: V2 still looked like a simplified generic OpenSCAD chair/stand rather than the racing seat phone stand in the reference photos.

Specific failures:

- seat shell still too slab-like
- side rail/truss base did not dominate the side silhouette enough
- roll cage path was still too generic
- phone placeholder transform needed a stricter fit check
- visual identity was improved but not acceptable

Fix:

- Created `openscad_rebuild_v3`.
- Wrote `WHY_V2_FAILED.md`.
- Built a new V3 SCAD file instead of patching V2.
- Rebuilt seat, rails/truss, and roll cage as separate photo-targeted systems.
- Fixed a V3 phone-placeholder floating bug found during side-view render review.

Rule: If a styled rebuild still looks wrong after a refinement pass, create a new version and explicitly document why the prior version failed.
