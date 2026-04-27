# Case Study: Command Link Base/Lid Fit Check

The Command Link enclosure uses separate SCAD files for the lower base and
relay lid. A fit-check SCAD imports fresh production STL exports for both parts
and overlays alignment helpers.

Pattern used:

- shared dimension file for body size, seal values, and fastener positions
- production STL export for each part
- verification SCAD imports those STLs
- fit modes for closed, exploded, cutaway, and alignment views
- visual helpers for O-ring, sealing land, screw axes, and PCB envelopes

Important lesson: a lid can look correct by itself and still fail assembly.
Always verify the actual mating position and fastener alignment.
