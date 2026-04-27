# Preview And Debug Helpers

Preview helpers prove serviceability and clearance. They should be optional and separate from production geometry.

## Useful Preview Types

- Transparent PCB placeholder.
- Wire zone markers.
- Zip-tie path blocks.
- Wire bundle cylinders or rectangles.
- Service clearance blocks.
- Screwdriver access cylinders.
- Grommet or cable gland hardware preview.
- Heat-set insert depth preview.
- Component height envelope.

## Toggle Pattern

```scad
show_pcb_placeholder = true;
show_zip_tie_path_preview = true;

module pcb_placeholder() {
    if (show_pcb_placeholder)
        %color([0.1, 0.45, 1.0, 0.25])
            translate([pcb_origin_x, pcb_origin_y, pcb_z])
                cube([pcb_width, pcb_length, pcb_thickness]);
}
```

## Preview Geometry Should

- Use `color()` with alpha.
- Use `%` for transparent background previews when helpful.
- Be turned on and off by parameters.
- Never be required for production geometry.
- Show the physical path of installation or use.

## Debug Modifiers

- `%` shows transparent background geometry.
- `#` highlights geometry in preview.
- `*` disables geometry temporarily.
- `!` shows only one branch for isolation.

## Serviceability Previews

For cable-tie saddles, preview:

- The zip-tie band path.
- The wire bundle.
- Clearance to PCB edge.
- Clearance to inside wall.

For screw bosses, preview:

- Screwdriver cylinder.
- Screw head clearance.
- Insert depth.

## Rule

Preview should answer a physical question. If it only makes the model look nicer, it is not a useful preview helper.
