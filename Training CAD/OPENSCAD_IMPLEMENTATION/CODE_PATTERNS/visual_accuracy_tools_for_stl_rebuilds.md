# Pattern: Visual Accuracy Tools For STL Rebuilds

## Preview Toggles

Use these toggles for styled STL rebuilds:

```scad
show_rebuild = true;
show_original_overlay = false;
show_comparison_planes = false;
show_phone_placeholder = false;
show_cutaway = false;
show_part_labels = false;
```

## Comparison Modules

```scad
module reference_overlay(part = "assembly") {}
module comparison_preview() {}
module phone_placeholder() {}
```

## Functional Placeholder Rule

If the model holds another object, create a placeholder for that object. For phone stands:

```scad
phone_width = 76;
phone_thickness = 12;
phone_height = 150;
phone_angle = 13;
```

The placeholder must visibly sit in the slot/lip/backrest geometry.

## Styled Seat Form Guidance

Use layered features:
- main shell silhouette
- raised cushion panels
- seam/groove strips
- bolsters as separate masses
- cutouts as subtractive rounded slots

## Rollcage Guidance

Use named tube points:
- feet
- rear hoop
- front legs
- side frames
- lower rails
- diagonal braces

Do not scatter diagonal lines without a structural reason.
