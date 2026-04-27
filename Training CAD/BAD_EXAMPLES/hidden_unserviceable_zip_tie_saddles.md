# Hidden / Unserviceable Zip-Tie Saddles

## Summary

A zip-tie saddle is still a bad design if it technically has a tunnel but cannot be reached after the PCB, wires, or other hardware are installed.

## Why It Matters

Wire strain relief is usually installed late in assembly, after wires are soldered or connected. If the saddle is hidden under the board edge, trapped behind a wall, or blocked by solder pads, the assembler has to thread the tie blindly or skip the strain relief entirely.

## Bad Pattern

- Saddle placed too close to the PCB edge.
- Tunnel hidden under wire pad zones or board overhang.
- No finger or needle-nose plier access.
- Tie path visible in CAD only when the PCB preview is hidden.
- Tie feature placed against the enclosure wall.

## Correct Design Rule

Check serviceability with the PCB installed. A usable tie feature needs a visible path, open approach clearance, and enough side space to feed and tighten a real tie.

## OpenSCAD/CAD Notes

Add preview geometry for the PCB, tie path, wire bundle, and service clearance zones. If the previewed tie path intersects the PCB, wall, standoffs, or solder-pad access zones, move the saddle or increase the side channel.

## Manufacturing Notes

Physical assembly should be tested with the actual zip tie, wire bundle, and PCB installed. Clearance that looks acceptable in CAD may be tight after FDM tolerance, wire stiffness, and hand access are included.

## Tags

bad-example, zip-tie, serviceability, pcb-carrier, wire-management
