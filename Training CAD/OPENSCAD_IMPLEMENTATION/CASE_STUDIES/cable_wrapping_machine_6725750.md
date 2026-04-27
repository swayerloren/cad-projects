# Case Study: Cable Wrapping Machine 6725750

## Problem

Rebuild a downloaded multi-part STL cable wrapping machine as editable, parametric OpenSCAD without raw mesh conversion.

## Useful Workflow

1. Inventory every STL and hash files to detect exact duplicates.
2. Record bounding boxes before interpreting function.
3. Fit cylindrical features to find posts, bores, rollers, collars, and shaft clearances.
4. Use bundled screenshots to separate print-bed coordinates from actual assembly logic.
5. Rebuild each part as a named module.
6. Add individual part previews and reference STL overlays.
7. Export rebuilt STLs and compare bounding boxes.
8. Document which values are measured and which are inferred.

## Mechanical Lessons

- C-shaped frames and ring gears allow side loading a cable without threading from the cable end.
- A top/bottom plate gearbox can constrain multiple printed gears without separate bearings.
- Glued printed standoffs are fast to assemble but poor for serviceability.
- Tape arms create cantilever load; their post roots need generous diameter and filleting.
- Gear train parameters should expose tooth count, outer diameter, root diameter, bore, height, and backlash allowance.

## OpenSCAD Lessons

- Keep source measurement arrays at the top of the file.
- Use simple parametric gear tooth polygons when exact involute teeth are not necessary for a study model.
- Add a numeric `preview_id` for Windows CLI render automation.
- Keep `import()` calls behind comparison toggles only.
