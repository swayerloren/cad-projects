# Serviceability Checks

Do not call a feature done just because it exists visually. It must be physically usable in the intended assembly sequence.

## OpenSCAD-Specific Checks

- Can the PCB drop in without colliding with guides, walls, saddles, or standoffs?
- Are screws reachable with a normal driver?
- Are heat-set inserts installable with vertical access?
- Can zip ties be inserted after the PCB is installed?
- Can wires bend from the grommet to solder pads?
- Can soldering still happen?
- Can a lid later be added?
- Are preview blocks intersecting production geometry?
- Are hidden features accidentally inside solids?

## Cable-Tie Saddle Sequence

The realistic assembly sequence is:

1. Install heat-set inserts.
2. Drop in PCB.
3. Screw PCB down.
4. Solder or connect wires.
5. Feed zip ties through strain-relief saddles.
6. Tighten zip ties around wire bundles.

If step 5 fails, the saddle is not serviceable.

## Preview-Based Checks

Use translucent placeholders for:

- PCB.
- Wire bundle.
- Zip-tie path.
- Clearance to wall.
- Clearance to board.

If a preview path intersects the board, wall, standoff, or solder zone, fix the geometry.

## Rule

A CAD feature is successful only when it supports the assembly process, the maintenance process, and the physical load path.
