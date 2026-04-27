# Case Study: COMMAND LINK External Mount Redesign

The COMMAND LINK rugged enclosure had external mounts that were still visually too complex after earlier cleanup. The mounts looked like stacked cylinders and trussed pods rather than real rugged electronics tabs.

Correction:

- Disabled the old mount layout from default geometry.
- Added a `simple_integrated_mount_ear()` path.
- Used four wide teardrop-style external tabs.
- Added one 4.3 mm screw clearance hole per ear.
- Replaced tall boss stacks with a 10 mm x 1.5 mm low boss.
- Moved gusseting into two simple side ribs so screw access stayed clear.

Lesson:

For rugged enclosure mounts, simple integrated geometry is usually better than visually busy ribs. Strength should come from tab thickness, neck width, boss bearing area, and direct wall/floor load path.
