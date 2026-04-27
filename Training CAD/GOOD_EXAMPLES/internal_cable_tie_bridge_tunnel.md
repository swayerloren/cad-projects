# Internal Cable-Tie Bridge Tunnel

## Summary

An internal cable-tie bridge tunnel uses floor-mounted side feet and a raised bridge so a real zip tie can pass under the bridge and loop over a wire bundle.

## Why It Matters

The feature transfers wire pull and vibration loads into the enclosure floor instead of the solder pads. Because it is internal-only, it does not create an exterior leak path.

## Good Pattern

- Floor-mounted low base pad.
- Two raised side feet or rails.
- Raised top bridge over the tie path.
- Real rectangular tunnel with visible entry and exit.
- Clearance preview showing the exact tie path.
- Placement outside the PCB outline and away from screw access.

## Correct Design Rule

Design the tie path first, then add material around it. A usable bridge is defined by the clearance volume that a real tie can pass through.

## OpenSCAD/CAD Notes

Use parameters for tunnel width, tunnel height, bridge thickness, bridge length, foot width, and feature count. Keep the clearance block in preview mode so it does not export as production geometry.

## Manufacturing Notes

Use enough bridge thickness to survive tie tension and vibration. Keep the tunnel height large enough for real printed tolerance and the actual tie band thickness.

## Tags

good-example, cable-tie, zip-tie, bridge-tunnel, wire-management, enclosure
