# Wall-Integrated Zip-Tie Bridge Slots

## Good Design

Use an internal wall pad with:

- upper inside-facing service slot
- lower inside-facing service slot
- smooth solid center bridge
- closed exterior wall behind the pad
- rounded/chamfered slot mouths
- a visible tie path preview during design

The tie should be feedable from inside the enclosure after the PCB is installed.

## Bad Design

Avoid:

- through-wall zip-tie slots
- standalone towers
- floor saddles trapped behind the PCB
- stacked rectangular blocks
- hard continuous rails that hide individual service features
- sharp slot edges that catch the zip tie

## Cut Depth Rule

Slot cutouts should remove only the inward bridge/pad projection. Do not cut into the exterior wall.

```scad
slot_cut_depth = min(pad_projection + 0.2, pad_projection - back_skin);
```

Keep the exterior wall thickness intact behind the pad.

## Audit Checklist

Before accepting a wall-integrated zip-tie bridge layout, verify:

- bridge count per wall and total bridge count
- slot width and height against the real zip tie
- path from upper slot to lower slot around the center bridge
- PCB edge clearance
- solder pad and wire-zone clearance
- standoff clearance
- top-rim and above-access clearance
- exterior wall integrity
- preview helpers excluded from production export

For compact PCB enclosures, preview the wire bundle, service lane, slot cutouts, and tie band together. A feature that looks plausible in isolation can still be unusable once the PCB and soldered wires are installed.

## Slot Mouth Quality

Avoid sharp rectangular cutter edges at the inside face. Use practical OpenSCAD approximations:

- rounded rectangle slot cutters
- shallow oversized slot-mouth cuts
- small corner reliefs
- pad edge radii
- individual pad blends instead of one hard continuous rail

The exterior wall must remain solid. Limit the slot cut depth to the inward pad/projection and leave backing material behind the slot.
