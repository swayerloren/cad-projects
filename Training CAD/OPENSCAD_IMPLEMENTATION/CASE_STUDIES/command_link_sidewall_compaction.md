# Case Study: COMMAND LINK Sidewall Compaction

Goal:

Reduce side width by aligning wall-integrated zip-tie clips and lid screw insert bosses.

Implementation:

- Added `side_wall_service_spine()`.
- Added `wall_integrated_lid_insert_boss()`.
- Added `wall_lid_boss_reinforcement()`.
- Updated shared lid/base fastener side inset from 10.0 mm to 8.0 mm.
- Reduced wire/clip side stack from 15.40 mm to 14.25 mm per side.
- Updated the lid because fastener positions moved.

Result:

The body width reduced from 95.80 mm to 93.50 mm while preserving the PCB mounting hole pattern, grommet, zip-tie clips, and O-ring interface.

Residual risk:

The integrated side zone locally interrupts the wire lane around lid bosses, so real harness routing must be checked with a physical print.
