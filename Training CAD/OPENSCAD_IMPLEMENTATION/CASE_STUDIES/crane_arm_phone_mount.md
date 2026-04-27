# Case Study: Crane Arm Phone Mount

## Project Type

Multi-part articulated phone/card/accessory mount rebuilt from STL references as parametric OpenSCAD.

## Key Observations

- Source STLs were already positioned in a shared coordinate space.
- Most articulated parts are thin plates with X/Z outlines and Y thickness.
- Pivot/screw holes cluster around D2.8 and D3.4.
- The project is a modular family: phone cradle, card holder, gripper linkage, webcam bracket, and lamp adapter.

## Rebuild Strategy

1. Measure every STL bounding box.
2. Fit cylindrical features by axis to identify screw and pivot holes.
3. Preserve the source coordinate convention for assembly preview.
4. Rebuild each part as a module with primitive hulls, plates, and cylinders.
5. Add adjustable phone and pivot parameters.
6. Keep STL imports behind overlay toggles only.

## Training Takeaways

- Do not force all STL files into one assumed product; group parts by functional subsystem.
- For articulated mounts, hole positions matter more than cosmetic pocket detail.
- Build a clean parametric approximation first, then document sculpted features that were not reproduced exactly.
