# Bad Example: Overworked Zip-Tie Slot Design

## Problem

The COMMAND LINK enclosure went through several generated zip-tie slot concepts that consumed space and visual complexity without reaching an acceptable result.

Rejected patterns included:

- long ladder/rack/grille side walls
- raised slot pods around every opening
- through-wall side slots that changed the exterior wall appearance
- preview paths that made the design look more resolved than the physical geometry
- repeated refinements that preserved the wrong design premise

## Lesson

When a small utility feature keeps getting worse through iteration, stop generating variations. Remove the failed feature, restore the main part to a clean state, and let the owner supply the next constraint or manual geometry.

## OpenSCAD Rule

Use a master feature gate for rejected experimental geometry:

```scad
show_zip_tie_features = false;

module rejected_feature_cutouts() {
    if (show_zip_tie_features) {
        // legacy cutouts only
    }
}
```

The default model must not contain rejected geometry.
