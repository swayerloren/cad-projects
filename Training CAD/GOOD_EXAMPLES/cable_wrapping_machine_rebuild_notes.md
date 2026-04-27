# Good Example Notes: Cable Wrapping Machine Rebuild

This project is a good example because it keeps the STL as reference only and creates editable modules for the functional forms:

- C-shaped frame plates
- standoff pattern
- spur gears
- crescent ring gear
- crank and handle
- tape roller and retaining collars

The most useful practice is the separation between:

- measured source facts
- inferred assembly positions
- simplified OpenSCAD geometry
- documented limitations

This separation prevents a parametric rebuild from pretending to be exact reverse engineering when only mesh and screenshots are available.
