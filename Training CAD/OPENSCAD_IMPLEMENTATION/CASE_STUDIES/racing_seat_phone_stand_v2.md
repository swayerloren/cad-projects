# Racing Seat Phone Stand V2 Case Study

## Source

Project:

```text
C:\Users\LJ\OpenSCAD Projects\pre made traiing models 3d\racing seat phone stand
```

V2 rebuild:

```text
openscad_rebuild_v2\scad\racing_seat_phone_stand_v2.scad
```

## Problem

Earlier rebuilds were too simplified. They did not fully capture the styled product identity: racing bucket seat, rail base, roll cage, truss web, harness openings, and real phone holder behavior.

## V2 Strategy

V2 uses:

- `racing_seat_shell()` for the bucket seat
- `head_harness_openings()` and `lower_harness_opening()` for real cutouts
- `front_phone_lip()` and `phone_placeholder()` for function validation
- `base_rail_assembly()` for side rails, screw holes, and truss webbing
- `tube_between_points()` for the roll cage
- `reference_stl_overlay()` and `comparison_preview()` for review

## Lessons

Styled product rebuilds need:

- silhouette review
- reference image inspection
- color/part separation
- functional placeholder checks
- overlay or side-by-side renders
- documentation of what remains simplified

## Remaining Limits

OpenSCAD can approximate organic sculpted seats, but exact seat shell curvature is better handled by loft/surface tools. For OpenSCAD, focus on silhouette, openings, bolsters, and function.
