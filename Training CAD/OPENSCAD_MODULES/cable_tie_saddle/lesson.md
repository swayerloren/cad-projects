# Cable Tie Saddle Lesson

## When To Use It

Use an internal cable-tie saddle when wires need strain relief inside an enclosure and exterior wall leak paths are not acceptable.

The preferred pattern is an open-top serviceable saddle in an accessible side channel. The tie enters one side, passes through a visible rectangular tunnel under the bridge, exits the other side, then loops around the wire bundle. The exterior wall stays solid.

Before finalizing the feature, check it with the PCB or nearby hardware installed. A saddle that works only when the PCB preview is hidden is not serviceable.

## Common Mistakes

- Tall unsupported zip-tie towers.
- Through-wall zip-tie holes.
- Tiny decorative slots.
- Blocky stacked geometry.
- Anchors placed where the PCB cannot be installed.
- Ambiguous rails where the zip tie path is not physically clear.
- Fake saddle shapes with no entry, no exit, or no visible clearance volume.
- Saddles hidden under or behind the installed PCB.
- Saddles too close to an inside wall for fingers or needle-nose pliers.

## Key Parameters

- `zip_tie_band_width`
- `zip_tie_band_thickness`
- `zip_tie_tunnel_clear_width`
- `zip_tie_tunnel_clear_height`
- `zip_tie_bridge_thickness`
- `zip_tie_bridge_top_height`
- `zip_tie_bridge_span`
- `zip_tie_bridge_length_along_y`
- `zip_tie_foot_width`
- `zip_tie_foot_length`
- `wire_lane_width`
- `clearance_from_pcb_edge`
- `clearance_from_inside_wall`

## Manufacturing Notes

Make the tunnel larger than the actual zip tie to allow for print tolerance. Use preview clearance blocks during review. Round or chamfer the bridge and feet to reduce stress and improve usability. Keep the bridge low enough for service access but high enough for a real tie tunnel. Test with the actual board, wire bundle, and zip tie installed.
