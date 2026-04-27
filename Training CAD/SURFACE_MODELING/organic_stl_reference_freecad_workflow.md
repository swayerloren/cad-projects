# Organic STL Reference FreeCAD Workflow

Use this workflow when an STL-derived product has organic or styled surfaces that are hard to recreate accurately in OpenSCAD.

## Workflow

1. Preserve original STL and photo references.
2. Import the STL into FreeCAD as a reference object.
3. Rebuild functional mechanical features as editable solids.
4. Use lofts, sweeps, and sketches for organic shells where practical.
5. Keep the imported mesh as reference when exact solid recreation would take too long.
6. Export production solids separately from reference meshes.
7. Document what remains approximate.

## Acceptance Rule

A model can be useful before it is visually exact, but it must be labeled honestly as partial if organic surface matching still needs manual review.

