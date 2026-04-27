# Case Study: Foot Pedal Switch STL Rebuild

## Context

A four-part foot pedal switch existed only as STL meshes:

- Lower base.
- Upper pedal shell.
- Ribbed grip plate.
- Spring cover strip.

The goal was not mesh conversion. The goal was to recover design intent and rebuild the parts as clean parametric OpenSCAD.

## Useful Workflow

1. List every STL and determine whether the project is an assembly.
2. Measure bounding boxes, mesh closure, component count, major planes, and repeated features.
3. Keep the original STL coordinate frames during early rebuild so overlay comparison is direct.
4. Rebuild with named parameters and modules.
5. Export individual parts and compare bounding box, area, and volume.
6. Document intentional mismatches.

## Design Lessons

- Wedge pedal bodies are often best modeled as XZ side profiles extruded across Y.
- Hinge pins should be modeled as real cylinder cuts through both mating parts.
- Switch pockets should remain serviceable; open rail pairs are often better than closed blocks.
- Repeated grip ribs should be measured by cross-section, not guessed from the height alone.
- Thin cover strips with latch recesses should use real stepped cuts, not surface decoration.

## Mistakes Caught

The grip ribs initially looked like half cylinders. That matched the bounding box but overestimated volume. Measuring the rib cross-section and extruding that profile matched the STL much more closely.

The first custom `polyhedron()` prism helper exported as non-closed geometry in CGAL. Replacing it with `linear_extrude()` for profile prisms produced clean solids.
