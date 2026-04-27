# Compact Wall-Integrated Zip-Tie Service Lane

## Summary

A wall-integrated zip-tie bridge should sit close to the PCB while preserving a real wire lane and service access.

## Why It Matters

Large empty side gaps make a housing look oversized and non-OEM. Compact electronics enclosures should calculate the clearance stack needed for the PCB edge, wire bundle, tie feature, and wall instead of using arbitrary large margins.

## Good Pattern

Use an explicit side stack:

```text
PCB edge -> small clearance -> wire lane -> tie clearance -> wall-integrated bridge pad -> wall
```

Example defaults:

- PCB clearance: 2.5 mm
- Wire lane: 6.0 mm
- Tie clearance: 0.4 mm
- Wall-tie pad projection: 2.2 mm
- Wall thickness: 3.5 mm

## Correct Design Rule

Serviceability must be preserved, but not by leaving a huge unused floor strip between the PCB and the wall.

## OpenSCAD / CAD Notes

- Define `compact_side_margin` from named clearance parameters.
- Use the calculated margin for both left and right carrier margins.
- Derive wire-lane X positions from the PCB origin and width.
- Show translucent wire-lane previews to confirm the lane is compact but usable.
- Keep the wall-tie pad projection small enough to look molded into the side wall.

## Manufacturing Notes

Print a small section with the wall bridge and wire lane if the zip tie or wire bundle is close to the limit. Keep enough tolerance for real wire insulation and imperfect FDM slots.

## Tags

zip-tie, wire-management, compact-enclosure, OpenSCAD, serviceability
