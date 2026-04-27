# Pattern: Articulated Mount Module Organization

## Recommended Parameters

```scad
phone_width = 78;
phone_thickness = 12;
pivot_hole_d = 3.0;
pivot_clearance = 0.25;
screw_hole_d = 2.8;
large_screw_hole_d = 3.4;
arm_thickness_y = 10;
thin_link_y = 3;
rib_thickness = 3;
```

## Recommended Modules

```scad
module base_mount() {}
module crane_arm() {}
module pivot_joint() {}
module phone_cradle() {}
module clamp_feature() {}
module screw_knob() {}
module reinforcement_ribs() {}
module assembly_preview() {}
module exploded_view() {}
module reference_stl(part) {}
module main() {}
```

## Geometry Pattern

For thin brackets where X/Z are the profile and Y is thickness:

```scad
module xz_plate(thick_y) {
    rotate([90, 0, 0])
        linear_extrude(height = thick_y, center = true)
            children();
}
```

Use this for arms, gripper jaws, and vertical bracket plates.
