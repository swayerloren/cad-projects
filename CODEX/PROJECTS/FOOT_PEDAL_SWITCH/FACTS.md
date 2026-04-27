# Facts

- Original STL files:
  - `Foot_Pedal_BottomV2.stl`
  - `Foot_Pedal_TopV2.stl`
  - `Foot_Pedal_plate.stl`
  - `Spring_CoverV2.stl`
- The project is a four-part print-layout assembly, not a single merged STL.
- Bottom/base bounding box: 151 x 96 x 29 mm.
- Top/pedal shell bounding box: 154.933 x 98 x 34.998 mm.
- Grip plate bounding box: 80 x 70 x 4.5 mm.
- Spring cover bounding box: 80 x 20 x 3 mm.
- Hinge bore center is X `61.5`, Z `8.0`, radius `2.5`, through Y.
- Switch rails run X `-35` to `0`, Z `3` to `29`, with two 3 mm diameter through holes.
- Grip plate has 12 ribs, 75 mm long, 5.5 mm pitch.
- Final SCAD exports matched all part bounding boxes exactly except the top shell Y size, which is within 0.21 mm.
