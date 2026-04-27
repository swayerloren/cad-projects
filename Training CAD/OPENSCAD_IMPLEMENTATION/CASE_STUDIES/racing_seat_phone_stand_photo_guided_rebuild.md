# Case Study: Racing Seat Phone Stand Photo-Guided Rebuild

The racing seat phone stand V2 had already improved on an earlier generic rebuild, but added reference photos provided sharper visual targets.

Photo evidence changed the rebuild priorities:

- Side view showed the seat back should lean farther back.
- Front/three-quarter views confirmed shoulder/head harness openings and a lower pass-through opening.
- Product views confirmed the phone is retained by a front lip and supported by the seat back.
- Side/base views confirmed long rails, screw holes, boss/washer pads, and triangular truss webbing.
- Roll cage views confirmed tube-like side/rear bracing, not random face-crossing bars.

OpenSCAD response:

- increased `seat_back_angle`
- increased `phone_lean_angle`
- kept the seat shell, base rails, and roll cage as separate modules
- added clearer wrapper modules for harness openings, bolsters, side rails, and screw details
- rendered assembly, front, side, and phone-fit views

Lesson:

For styled products, photos define acceptance criteria that STL bounding boxes cannot cover. Use photo review reports as part of the rebuild deliverable.
