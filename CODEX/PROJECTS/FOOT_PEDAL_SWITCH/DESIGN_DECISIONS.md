# Design Decisions

- Keep the original STL coordinate frame in the rebuild so `show_reference_stl=true` overlays directly.
- Rebuild the lower base from a 3 mm floor, wedge side profiles, a rear wall, a hinge crossbar, switch rails, and real cutouts.
- Model the upper shell as an outer XZ profile extruded along Y, then subtract an inner XZ profile to make a hollow pedal body.
- Use real cylinders for hinge and switch holes.
- Rebuild the grip ribs from a measured profile rather than generic half cylinders.
- Keep the spring cover as a separate service part with repeated stepped recesses.
- Export both a combined print-layout STL and individual rebuilt part STLs.
