# Floor-Mounted Zip-Tie Tunnels Trapped Beside PCB

## Summary

Floor-mounted zip-tie tunnels can fail serviceability when they sit in a narrow channel beside an installed PCB.

## Why It Matters

A tie feature that looks correct before assembly can become unusable after the board and soldered wires are installed. If the user must blindly feed a zip tie beside the PCB edge, the feature is not production quality.

## Bad Pattern

- Tunnel sits low on the floor beside the PCB.
- Tie path is partly hidden by the PCB edge or wire pad zones.
- User cannot easily reach the entrance and exit after soldering wires.
- Feature exists visually but is difficult to use.

## Correct Design Rule

Wire retention must be accessible in the actual assembly state: PCB installed, wires soldered, and tools approaching from above/inside the enclosure.

## OpenSCAD / CAD Notes

- Use PCB placeholders and wire-zone markers during review.
- Preview the actual tie path, not just the solid feature.
- If the tie path is hidden under or behind installed parts, redesign the feature.
- For sealed housings, prefer internal wall-integrated bridge slots that leave the exterior wall solid.

## Manufacturing Notes

Serviceability should be tested with the actual zip tie and wire bundle. A small printed coupon is useful before committing the full enclosure.

## Tags

bad-example, zip-tie, serviceability, PCB-enclosure, strain-relief
