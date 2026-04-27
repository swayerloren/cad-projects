# Internal Wall-Integrated Zip-Tie Bridge

## Summary

A production-minded wire strain-relief feature can be molded into the inside wall of an electronics enclosure without cutting through the exterior wall.

## Why It Matters

Vehicle and outdoor electronics often need dust and water resistance. Zip-tie holes through the exterior wall create leak paths, while floor-mounted saddles can become hard to reach after the PCB is installed. An internal wall bridge keeps the outside wall solid and leaves the tie path visible from inside.

## Good Pattern

- Raised pad molded onto the inside wall.
- Upper inside-facing slot.
- Lower inside-facing slot.
- Solid center bridge between the slots.
- Cutouts limited to the inward pad body.
- Translucent preview showing the tie route.

## Correct Design Rule

The zip tie must be installable after the PCB is installed, and the slot cuts must not enter the exterior wall.

## OpenSCAD / CAD Notes

- Model the exterior wall as one body.
- Model the inward bridge pad as a separate body.
- Use `difference()` only inside the pad module for the upper and lower slots.
- Do not include the wall in the same slot-cut `difference()` scope.
- Add preview blocks for the tie band and wire bundle.

## Manufacturing Notes

Keep enough pad projection and center bridge thickness for printed strength. Chamfer slot edges when possible, but do not make slots smaller than the actual zip-tie band plus tolerance.

## Tags

zip-tie, strain-relief, enclosure, wall-integrated, OpenSCAD, waterproofing
