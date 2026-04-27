# OpenSCAD Code Standards

OpenSCAD examples should be clean, reusable, and easy to modify.

## Required Practices

- Put major parameters at the top.
- Use modular code.
- Use meaningful module names.
- Avoid hidden critical dimensions inside modules.
- Keep source facts separate from assumptions.
- Comment coordinate systems.
- Include clean preview helpers.
- Keep examples valid OpenSCAD.
- Avoid fragile boolean geometry.
- Use reusable modules.
- Update lessons when a module improves.
- Remove dead compatibility wrappers, unused parameters, and rejected design modules during production-refinement cleanup.
- Organize larger files by feature ownership so parameters and modules follow the same architecture.

## Parameter Style

Use parameter names that describe design intent:

```scad
mount_hole_diameter = 4.2;
boss_outer_diameter = 11.0;
wall_thickness = 3.5;
```

Avoid magic numbers in geometry operations unless they are small render tolerances and are commented.

## Module Style

Good module names:

- `rounded_block()`
- `cable_tie_saddle()`
- `rounded_mount_ear()`
- `heat_set_insert_boss()`
- `grommet_entry()`
- `reinforcement_rib()`

## Preview Style

Examples may include a final call that renders a sample module.

Keep preview code separate from reusable module definitions when possible.

During final consolidation, keep only the current accepted modules. Do not leave old rejected geometry behind under compatibility names, because future prompts may accidentally reuse it.

## Geometry Style

Prefer simple robust geometry:

- `hull()` for rounded or blended forms.
- `difference()` for holes and tunnels.
- Small tolerances for clean booleans.
- Rounded rectangles for lugs and pads.

Avoid over-nested booleans and tiny features likely to fail in print.
