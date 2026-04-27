# Style Notes

The design language is motorsport/racing:

- bucket seat silhouette
- shoulder bolsters
- side bolsters
- harness slots
- cushion segment lines
- red truss rail base
- black rollcage

The phone stand function is integrated into the seat form: the front lip and seat pan hold the phone bottom edge, while the backrest defines the viewing angle.

The rebuild simplifies organic curves into parametric profiles and tube segments.

## Refinement Pass Notes

The previous rebuild was too simplified. The corrected style target is:
- recognizable bucket seat, not a flat slab
- shoulder wings and side bolsters with visible mass
- cushion panel seams and harness slots
- clear phone cradle lip/slot
- base that reads like a red racing chassis/truss
- rollcage with purposeful hoop and bracing layout

Remaining limitation: OpenSCAD can approximate the sculpted racing seat style, but exact organic surface blends from STL are still not practical without a loft/surface workflow.

## V2 Style Target

V2 must read immediately as a miniature racing seat phone stand:

- red racing bucket seat shell
- black cushion insert
- shoulder/head harness slots
- lower harness/pass-through slot
- red front phone catch/lip
- gray side rails with screw/bolt holes
- black triangular truss webbing
- black roll cage tube frame
- rear hoop and diagonal braces

Do not accept a rebuild that looks like a generic phone chair. The visual identity depends on silhouette, color-separated parts, tube-frame geometry, rail/truss base, and the phone placeholder fit check.

## Reference Photo Pass - 2026-04-26

New photos in the V2 source folder are now the primary style target. Three JPEGs were decoded and reviewed; one AVIF was found but not decoded by local tooling.

Photo-confirmed style requirements:

- bucket seat shell with a reclined backrest, rounded side bolsters, shoulder/head openings, lower pass-through opening, and front phone catch
- black or dark inset cushion area
- gray/white side rails with screw/bolt holes and boss/washer pads
- triangular truss webbing along the base/side rail structure
- black round-tube roll cage with rear hoop, rear upright, lower side rail, and side/rear diagonal braces

Future styled rebuilds must use reference photos to check silhouette, color/part separation, and visible function before claiming visual accuracy.

## V3 Style Notes

V3 style target:

- bucket shell must be the primary red mass
- shoulder harness openings must remain visible in front view
- dark cushion insert must not cover the harness openings
- side rails must sit beside the seat and show screw tabs/boss rings
- triangular side truss webbing must be visible in side view
- roll cage must read as black round tube with rear hoop and diagonal braces
- phone placeholder must sit in the bucket area, not float above it

V3 is more recognizable than V2, but the organic molded seat surface is still approximate.
