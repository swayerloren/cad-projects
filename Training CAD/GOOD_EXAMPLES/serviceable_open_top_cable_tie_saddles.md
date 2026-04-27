# Serviceable Open-Top Cable-Tie Saddles

## Summary

A serviceable open-top cable-tie saddle can be threaded after the PCB is installed and wires are connected.

## Why It Matters

In electronics enclosures, strain relief must be usable during real assembly, not only visible in the CAD model. Serviceable saddles protect solder joints from vibration and wire pull without creating exterior wall leak paths.

## Good Pattern

- Saddles sit in the open channel between PCB edge and inside enclosure wall.
- Each saddle has two floor-mounted feet and a raised bridge.
- The tunnel is visible and accessible from above.
- There is clearance from the PCB edge and from the inside wall.
- Preview helpers show tie path, wire bundle, and service clearances.
- Exterior walls remain solid.

## Correct Design Rule

Design the assembly sequence first: install PCB, solder/connect wires, feed zip ties, tighten strain relief. The saddle geometry must support that sequence.

## OpenSCAD/CAD Notes

Use parameters for tie band size, tunnel clearance, bridge height, saddle span, side clearance to PCB, and side clearance to wall. Use preview-only translucent blocks or cylinders to review the service envelope.

## Manufacturing Notes

For FDM prints, make tunnel height and side clearances larger than nominal tie dimensions. Test with real pliers and the actual wire bundle.

## Tags

good-example, zip-tie, serviceability, wire-management, pcb-carrier, enclosure
