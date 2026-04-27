# COMMAND LINK Mount Ear Refinement

## What Failed

The initial external mounts went through several rejected forms:

- Weak flat ears.
- Chunky reinforced pods.
- Rough truss/fork shapes.
- Patch-like geometry that did not look OEM.

## Better Direction

The accepted direction is a clean automotive-style mount:

- Rounded oval or teardrop lug.
- Centered screw clearance hole.
- Raised boss/ring around the hole.
- Wide neck into the enclosure wall/floor.
- Small number of clean gussets.
- No decorative fin farm.

## OpenSCAD Modules

Use separate modules:

```scad
module rounded_mount_ear(side, y) { ... }
module mount_ear_boss(side, y, cut = false) { ... }
module mount_ear_gussets(side, y) { ... }
module refined_mount_ear(side, y, cut = false) { ... }
module refined_mount_layout(cut = false) { ... }
```

## Boss / Hole Logic

The screw hole should be a cut module used inside the main `difference()`:

```scad
difference() {
    refined_mount_layout(false);
    refined_mount_layout(true);
}
```

This keeps the visual boss and the clearance hole aligned.

## Avoiding Ugly Geometry

- Do not add random ribs after the fact.
- Do not make fork-shaped tabs unless required by the load path.
- Use `hull()` for rounded lugs and smooth necks.
- Use simple gussets that connect wall/floor to the boss region.

## Rule

External mounts should look like one molded feature integrated into the body, not a bracket glued onto a box.
