# Serviceable Ribbed Foot Pedal Design

Lessons from rebuilding a foot pedal switch in OpenSCAD.

## Printability

- Use 3 mm class wall and floor thickness for durable FDM pedal shells unless the design has another validated thickness.
- Align hinge bores so they can be cleaned with a drill or pin after printing.
- Avoid fragile thin towers around the switch. Tie switch rails into the floor.
- Keep long sloped shells as simple extruded profiles where possible.

## Grip Ribs

Grip ribs should be modeled from a measured or named profile.

Do not assume every raised rib is a half cylinder. In the case study, half cylinders matched height but added too much volume. A measured circular-segment profile matched the STL.

## Serviceability

- Separate grip plates can be replaced without reprinting the whole pedal.
- Separate spring covers preserve access to internal hardware.
- Open switch pockets support inspection and replacement.
- Rear wire exits should be real cutouts with clearance, not only visual grooves.
