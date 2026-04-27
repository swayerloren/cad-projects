# Tunnels, Slots, And Cutouts

This section is critical for wire-management features. A zip-tie saddle must have a physically usable tunnel, not just a visual notch.

## A Real Tunnel Must Have

- An entrance.
- An exit.
- Clear width larger than the zip-tie band.
- Clear height larger than the zip-tie thickness plus print tolerance.
- A cut that fully passes through the bridge body.
- Placement that remains accessible after assembly.

## Zip-Tie Saddle Rules

- The tunnel must be visible and accessible after PCB installation.
- The tunnel must not be hidden under the PCB edge.
- The tunnel must not be blocked by solder pads, standoffs, or walls.
- The tunnel must not cut through the exterior wall.
- Preview geometry should show the actual zip-tie path.

## Bad Patterns

- Blocky saddle with no actual through path.
- Shallow notch that cannot pass a tie.
- Slot hidden under the board edge.
- Tunnel too close to the wall for fingers or pliers.
- Cut module that does not cut fully through the bridge.
- Through-wall slot that creates a leak path.

## Good Pattern

- Open-top serviceable bridge saddle.
- Two raised feet on the floor.
- Raised bridge across the feet.
- Real rectangular tunnel cut through the bridge.
- Clearance from PCB edge.
- Clearance from inside wall.
- Translucent zip-tie path preview through the tunnel.

## Wall-Integrated Bridge Pattern

For a dust/water resistant enclosure, a better pattern may be an internal wall-integrated bridge:

- Mold a pad onto the inside wall.
- Cut an upper inside-facing slot through the pad.
- Cut a lower inside-facing slot through the pad.
- Leave a solid center bridge between the two slots.
- Feed the zip tie from inside through the upper slot, around/behind the center bridge, and out the lower slot.
- Keep all slot cutouts inside the inward pad body.
- Do not subtract the slot cutouts from the exterior wall.

This pattern works when a floor-mounted saddle would be hard to reach after the PCB is installed. The critical OpenSCAD rule is to keep the wall and the slotted pad as separate solids, then apply `difference()` only inside the pad module.

## Compact Wall Service Lane

Do not solve tie access by making the enclosure side channel arbitrarily wide. Calculate the side margin from the physical stack:

```scad
wire_lane_clearance_from_pcb = 2.5;
wire_lane_width = 6.0;
wire_lane_to_tie_clearance = 0.4;
wall_tie_pad_projection = 2.2;
wall_thickness = 3.5;

compact_side_margin =
    wall_thickness
    + wall_tie_pad_projection
    + wire_lane_to_tie_clearance
    + wire_lane_width
    + wire_lane_clearance_from_pcb;
```

Then derive the wire lane positions:

```scad
function left_wire_lane_x() =
    pcb_origin_x - wire_lane_clearance_from_pcb - wire_lane_width;

function right_wire_lane_x() =
    pcb_origin_x + pcb_width + wire_lane_clearance_from_pcb;
```

Use preview blocks for both the tie path and the wire lane. If the preview shows a large dead floor strip between the PCB and wall feature, the enclosure is probably too wide.

## Pass / Fail Checklist

1. Can the zip tie be inserted after the PCB is installed?
2. Can you see the tunnel in the review model?
3. Is there clearance on both sides of the saddle?
4. Does the tunnel cut only the internal saddle and not the wall?
5. Does the preview zip tie intersect any production solid?
6. Can the tie loop over the wire bundle and tighten?
7. Can fingers or needle-nose pliers reach the tie?
8. If the feature is wall-integrated, does the exterior wall remain solid behind the slots?

## OpenSCAD Pattern

```scad
module tunnel_cut() {
    translate([-clear_w / 2, -path_len / 2 - 0.2, -0.02])
        cube([clear_w, path_len + 0.4, clear_h + 0.04]);
}

module saddle() {
    difference() {
        union() {
            left_foot();
            right_foot();
            bridge();
        }
        tunnel_cut();
    }
}
```

## Wall-Integrated Slot Pattern

```scad
module wall() {
    cube([wall_thickness, wall_length, wall_height]);
}

module internal_bridge_pad() {
    difference() {
        cube([pad_projection, pad_width, pad_height]);
        upper_slot_cut();
        lower_slot_cut();
    }
}

module wall_integrated_tie_bridge() {
    union() {
        wall();
        translate([wall_thickness, pad_y, pad_z])
            internal_bridge_pad();
    }
}
```
