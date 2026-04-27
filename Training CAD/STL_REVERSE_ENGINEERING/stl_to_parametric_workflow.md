# STL To Parametric Workflow

The goal of STL reverse engineering is a clean parametric model, not a noisy copy of mesh triangles.

## Workflow

1. Preserve the original STL and any photos, README files, or STEP files.
2. Identify functional interfaces first: holes, shafts, hinges, screw patterns, tabs, clips, mating faces, and clearances.
3. Measure bounding dimensions only as a starting point.
4. Rebuild mechanical features as named parameters.
5. Use OpenSCAD for repeated mechanical structure.
6. Use FreeCAD when the part needs sketches, fillets, chamfers, STEP output, or surface control.
7. Compare the rebuild against the reference with screenshots or overlays.
8. Record misses, corrections, and final dimensions in project memory.

## Avoid

- Rebuilding only the bounding box.
- Copying organic mesh noise into parametric CAD.
- Ignoring reference photos.
- Exporting preview reference geometry as production STL.
- Treating decorative surface shape as more important than mechanical fit.

