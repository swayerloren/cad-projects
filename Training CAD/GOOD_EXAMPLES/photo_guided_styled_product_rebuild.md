# Good Example: Photo-Guided Styled Product Rebuild

A styled STL rebuild should be checked against reference photos before it is called accurate.

Good workflow:

- inventory STLs and photos
- inspect each photo for visible view angle, colors, silhouette, holes, supports, and user-facing function
- compare the current OpenSCAD model against photo-visible requirements
- update parameters and modules based on evidence, not guesses
- render assembly, front, side, and functional placeholder views
- document what still cannot be confirmed

For the racing seat phone stand V2, the photos confirmed the critical identity: bucket seat shell, harness holes, front phone catch, gray side rails, screw bosses, triangular truss webbing, and a black tube roll cage.

Acceptance test: the rebuilt model should be recognizable from the same views as the photos, and the functional placeholder should sit the way the product is meant to be used.
