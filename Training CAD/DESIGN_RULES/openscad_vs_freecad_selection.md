# OpenSCAD Vs FreeCAD Selection

Use OpenSCAD when the design is naturally parameterized, mechanical, repeatable, and mostly made from primitives, boolean operations, hulls, and reusable modules.

Good OpenSCAD fits:

- enclosures
- PCB carriers
- holes and hole patterns
- ribs and gussets
- brackets and mounts
- bosses and heat-set insert features
- cable tie saddles, clips, and wire guides
- production STL exports

Use FreeCAD when the design needs richer solid modeling, sketches, constraints, fillets, chamfers, assemblies, STEP output, or surface control.

Good FreeCAD fits:

- constrained sketches
- feature trees
- STEP-first workflows
- precise fillets/chamfers
- mating assemblies
- imported STEP inspection
- macro-driven solid CAD
- surface-heavy or organic references

Selection rule:

- Start in OpenSCAD for code-driven mechanical systems.
- Start in FreeCAD for sketch/constraint-driven solid CAD or STEP deliverables.
- Use both when OpenSCAD handles repeatable structure and FreeCAD handles final solid modeling or export requirements.

