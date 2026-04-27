# Huge Wall-To-PCB Gap For Zip-Tie Access

## Summary

Leaving a large empty gap between the PCB edge and the inside wall is a poor way to make zip-tie features accessible.

## Why It Matters

Oversized gaps make an enclosure look crude, waste print time, and can make wire routing less controlled. A rugged part should be compact and intentional, not simply made wider to avoid solving serviceability.

## Bad Pattern

- PCB edge far from inside wall.
- Wall-retention feature sits behind a large dead floor strip.
- Wire lane is not clearly defined.
- Housing becomes wider than needed.
- Geometry looks like a wall rail added after the fact.

## Correct Design Rule

Calculate the side spacing from the actual service lane requirements: PCB clearance, wire lane, tie feature projection, and wall thickness.

## OpenSCAD / CAD Notes

- Avoid hard-coded side margins such as `carrier_margin_left = 26` unless that size is justified.
- Use named parameters such as `wire_lane_width`, `wire_lane_clearance_from_pcb`, and `wall_tie_pad_projection`.
- Add preview blocks for the wire lane and tie path.

## Manufacturing Notes

Compact does not mean tight. Keep enough tolerance for real wires, zip ties, fingers, and tools, but remove dead space that serves no assembly or structural purpose.

## Tags

bad-example, enclosure, zip-tie, OpenSCAD, compactness
