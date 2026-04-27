# Code Pattern: Photo Reference Review Workflow

Use this workflow when an STL rebuild also has reference photos.

1. List every photo file and whether it can be decoded locally.
2. For each readable photo, record view angle, visible colors, visible parts, functional contact points, fasteners, holes, and supports.
3. Make a comparison table:

```text
Feature | Photo evidence | Current model status | Result | Required change
```

4. Update OpenSCAD parameters only where the photo gives evidence.
5. Add or rename modules so the code reflects photo-visible features.
6. Render the same viewpoints the photos show.
7. Render a functional placeholder view for stands, holders, fixtures, mounts, and cradles.
8. Document limitations and any files that could not be decoded.

For phone stands, the placeholder should verify the actual contact path: bottom catch, back support, side clearance, and charging/cable access if visible.
