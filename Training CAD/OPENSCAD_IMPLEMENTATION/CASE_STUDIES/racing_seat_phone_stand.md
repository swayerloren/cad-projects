# Case Study: Racing Seat Phone Stand

## Project

Three-part styled phone stand rebuilt from STL references:
- racing seat shell
- flat truss base
- rollcage frame

## Workflow Lessons

1. Render each STL individually before interpreting the assembly.
2. Measure bounding boxes for every part.
3. Split the design into functional geometry and style geometry.
4. Rebuild the functional cradle first: seat pan, front lip, backrest, phone slot, cable notch.
5. Add style: bolsters, harness slots, cushion seams, base trusses, rollcage.
6. Compare exported rebuilt STLs against original envelopes.

## OpenSCAD Lessons

- Use extruded 2D profiles for seat shells and base rails.
- Use point-to-point cylinders for tube frames instead of sphere hulls when performance matters.
- Expose style parameters, not only mechanical dimensions.
- Keep STL imports as overlays only.
