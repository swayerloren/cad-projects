# Foot Pedal Hinge and Switch Mounts

Lessons from the foot pedal switch rebuild.

## Hinge Pattern

A printable foot pedal hinge can be represented as:

- A rectangular front crossbar or paired knuckles.
- A straight cylindrical bore through the full hinge axis.
- A shared pin center between the base and pedal shell.
- Enough wall around the bore for wear and print tolerance.

Record the hinge center as a named parameter. In the case study the hinge axis was X `61.5`, Z `8.0`, radius `2.5`, through Y.

## Switch Rail Pattern

Open switch rails are serviceable and easy to model:

- Use two parallel rails instead of a closed pocket when access matters.
- Keep rail thickness explicit.
- Cut fastener or retention holes as cylinders through both rails.
- Leave the central switch body space open.

Avoid burying switch dimensions inside one-off cubes. Name rail length, rail thickness, rail gap, hole centers, and hole radius.

## Practical Checks

- Verify that hinge and switch holes are actual boolean cuts.
- Check wall thickness around holes after subtracting.
- Export the part and compare volume after adding bosses or rails.
- Keep removable covers and grip surfaces as separate parts when serviceability matters.
