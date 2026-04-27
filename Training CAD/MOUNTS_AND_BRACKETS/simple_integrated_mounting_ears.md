# Simple Integrated Mounting Ears

Use this pattern for rugged enclosures, PCB carriers, and small vehicle electronics modules.

Recommended defaults:

```scad
mount_ear_length = 18;
mount_ear_width = 16;
mount_ear_thickness = 5;
mount_hole_diameter = 4.3;
mount_boss_outer_diameter = 10;
mount_boss_height = 1.5;
mount_neck_width = 16;
mount_neck_length = 8;
mount_gusset_thickness = 3;
mount_gusset_height = 7;
mount_gusset_length = 10;
```

Design notes:

- Keep the tab wide enough for a washer or screw head.
- Keep the neck as wide as the tab where possible.
- Use a low boss/ring, not a tall stack.
- Keep ribs away from the screw hole.
- Prefer one or two simple ribs over decorative trusses.
- Check screw access from above before calling the mount serviceable.
