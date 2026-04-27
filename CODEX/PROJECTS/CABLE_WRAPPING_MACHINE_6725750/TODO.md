# TODO

- Replace simplified gear teeth with true involute gears if functional printing is required.
- Add explicit backlash parameters for every gear mesh.
- Add optional screw/heat-set-insert serviceable frame variant.
- Add washer clearances between gears and plates.
- Verify actual gear center distances from the creator video or a fully assembled reference if available.
- Add a cable diameter parameter and tape roll width parameter.
- Consider adding animation states for ring rotation and crank rotation.

## Added after mechanical correction pass

- Physically verify backlash for drive-to-driven and connecting-to-ring meshes.
- Confirm ring gear pitch diameter from original CAD, creator notes, or print test.
- Confirm exact tape arm operating angle and tape roller position during wrapping.
- Add an optional animated preview showing crank, driven gears, connecting gears, and ring gear rotation.
- Add a serviceable hardware variant with shoulder screws or metal dowel pins.
- For future STL rebuild reviews, require `MECHANICAL_ACCURACY_REVIEW.md` before accepting any gear-driven machine.
