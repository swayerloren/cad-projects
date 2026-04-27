# Common OpenSCAD Failures

## Geometry Failures

- Non-manifold geometry.
- Coincident faces and z-fighting.
- Cutouts not long enough.
- Negative dimensions from bad parameter math.
- Undefined variables.
- Too many nested booleans.
- Slow or oversized `minkowski()` operations.
- Hidden geometry inside solids.

## Functional Failures

- Fake holes or slots that do not actually cut.
- Tunnels with no entrance or exit.
- Preview-only features accidentally included in production geometry.
- Wrong coordinate mapping.
- Mirrored left/right features placed on the wrong side.
- Board installed but service features blocked.
- Internal tie features cutting through exterior walls.

## Debug Habits

- Render small modules alone.
- Use `%` placeholders to check interference.
- Add temporary cutaways.
- Echo derived dimensions if needed.
- Verify F6 render, not only F5 preview.
- Check for old rejected module names after refactors.

## Parameter Math Risks

Guard derived dimensions with `max()` when a user-adjustable parameter could make a negative cube size.

```scad
cube([max(0.1, usable_width), depth, height]);
```

Do not hide a bad layout by clamping everything. Use clamps to prevent render failure, then fix the design.
