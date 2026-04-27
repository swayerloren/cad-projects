# Case Study: COMMAND LINK Rugged Lid Design

The COMMAND LINK lower enclosure needed a top half that did more than close the box. The lid had to carry automotive relays, support serviceable brackets, and start a sealing strategy.

Implementation choices:

- created a separate `command_link_rugged_lid.scad`
- duplicated mating dimensions from the active lower enclosure instead of including the lower SCAD, because the lower file has a top-level assembly call
- used preview/production modes
- made preview helpers for lower-base reference, relays, O-ring, and insert depths
- created a first-pass O-ring groove and downward lip
- used six lid screw clearance holes
- used ten underside insert bosses for five relay brackets
- added underside ribs around relay boss pairs

Key lesson:

A lid that carries relays is an assembly component. The CAD must show relay envelopes, bracket insert positions, seal path, fastener strategy, and the lower-base updates still required.
