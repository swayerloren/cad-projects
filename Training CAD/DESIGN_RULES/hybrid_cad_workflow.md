# Hybrid CAD Workflow

A hybrid workflow uses the tool that fits each part of the job instead of forcing all geometry through one CAD system.

## Common Flow

1. Use STL, STEP, photos, or hardware measurements as references.
2. Rebuild repeatable mechanical structure in OpenSCAD when parametric code is clearer.
3. Use FreeCAD when sketch constraints, fillets, chamfers, assemblies, or STEP export matter.
4. Export clean deliverables from the tool best suited to the final manufacturing path.
5. Record source paths, parameters, and decisions in `CODEX\PROJECTS`.
6. Convert reusable lessons into `Training CAD`.

## When To Split Work

Split work across tools when:

- OpenSCAD preview geometry is useful but final STEP is required.
- A part has repeated mechanical features plus sculpted or filleted surfaces.
- FreeCAD can import and inspect a reference mesh more effectively.
- A project needs both code-driven variants and manufacturable solid CAD output.

Keep project notes explicit about which tool is authoritative for each deliverable.

