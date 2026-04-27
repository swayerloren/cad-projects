# Assembly Notes

- The source STLs are arranged for printing, not assembled in place.
- Base and top plate match by mirrored Y alignment of standoff holes.
- Five standoff locations tie the two plates together.
- Two larger D14 shaft holes are present in the base/top plate pattern.
- The gear train placement in the OpenSCAD assembly is inferred from source images and part function.
- The ring gear and tape arm are the core wrapping mechanism.
- The crank and handle are attached to the drive gear axis in the preview.
- The source README says superglue is used, so the original is probably not designed for repeated disassembly.

## Corrected assembly model - 2026-04-26

- The machine should be modeled as a stacked gear train, not as all gears on one arbitrary level.
- The two measured shaft holes in the frame are shared axes:
  - upper plane: medium driven gears
  - lower plane: small connecting gears
- The drive gear sits on the gear block/crank axis and meshes with both driven gears.
- The ring gear sits in the lower plane and meshes with the two connecting gears.
- The tape arm sits on the ring gear pin above the top plate.
- Cable/tape path preview should be present during review so function is visible.
