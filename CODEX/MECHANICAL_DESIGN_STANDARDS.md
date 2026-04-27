# Mechanical Design Standards

This file defines the mechanical design standards Codex must follow when generating or modifying 3D printed, CNC, OpenSCAD, enclosure, bracket, electronics housing, or injection-molded parts.

Do not create weak hobby-grade geometry unless the part is clearly low-load.

Always design like a mechanical product designer.

---

## Core Design Mindset

Every part must be:

- strong enough for its real environment
- printable or manufacturable
- serviceable
- compact where possible
- clean and intentional
- parameterized when coded
- based on real dimensions
- documented when assumptions are made

Avoid:

- random blocks
- weak flat plates
- unsupported posts
- thin cantilever tabs
- decorative ribs that do nothing
- oversized bulky geometry with no structural reason
- exterior holes unless they are intentional
- geometry that looks good only in the render but fails in real use

---

## Required Design Workflow

Before generating or modifying a part:

1. Identify the exact part purpose.
2. Identify real loads:
   - screw clamping
   - vibration
   - shock
   - bending
   - twisting
   - wire pull
   - impact
   - heat
   - assembly force
3. Identify fixed dimensions from source files.
4. Separate confirmed facts from assumptions.
5. Determine manufacturing method:
   - FDM 3D print
   - resin print
   - CNC
   - laser cut
   - injection molded
   - hybrid/prototype
6. Design the load paths first.
7. Add ribs, gussets, bosses, and transitions only where useful.
8. Check serviceability.
9. Check printability/manufacturability.
10. Review against known project errors before finalizing.

---

## Load Paths

Every structural feature must have a clear path for force to travel into the stronger body of the part.

Fastener loads should flow into:

- bosses
- ribs
- walls
- floors
- reinforced corners
- broad mounting necks

Wire strain should flow into:

- internal strain relief
- cable saddles
- zip-tie anchors
- wire channels
- grommets or cable glands

Shock and vibration loads should not be carried by:

- thin cantilever tabs
- tall unsupported posts
- isolated bosses
- sharp inside corners
- small unsupported wall sections

Bad design:

- flat ear sticking out from a wall
- screw hole in a thin tab
- zip-tie tower with no gussets
- standoff cylinder with no base support

Good design:

- rounded mount ear with wide neck
- boss with ribs into wall/floor
- triangular gussets at loaded transitions
- reinforced cable saddle molded into the floor or wall
- screw load distributed through a boss and base pad

---

## Truss, Rib, Gusset, and Lattice Thinking

For vibration, shock, and weight-conscious design, triangular load paths are usually better than unsupported rectangles.

Use:

- triangular gussets
- diagonal ribs
- V-shaped bracing
- X-shaped bracing
- ribbed load paths
- reinforced boss-to-wall transitions
- lattice/web structures where they are actually useful

Do not use decorative trusses or lattices.

A rib, truss, or lattice must connect real load-bearing features.

If it does not transfer force, stiffen a weak area, or protect against bending/twisting, remove it.

---

## Ribs

Use ribs to stiffen large flat areas, walls, brackets, tabs, and bosses.

Good ribs:

- connect structural features
- follow the direction of load
- reduce flex
- avoid blocking assembly
- are thick enough to print
- have softened transitions where practical

Bad ribs:

- floating decorative strips
- extremely thin fins
- random fin farms
- ribs that block screws or wires
- ribs that create impossible support removal
- ribs that make injection molding worse without benefit

Typical guidance:

- 3D printed rugged ribs: usually 2.0 mm to 4.0 mm thick
- injection-molded ribs: often 40% to 70% of nominal wall thickness
- rib height should be useful but not so tall it becomes fragile
- rib bases should be blended or chamfered when practical

---

## Gussets

Use gussets where vertical and horizontal features meet.

Add gussets around:

- PCB standoffs
- screw bosses
- heat-set insert bosses
- mounting ears
- brackets
- zip-tie anchors
- wall-to-floor joints
- connector supports
- cable gland bosses

Good gussets:

- form triangular load paths
- reduce flex
- tie the feature into the main body
- avoid sharp internal crack points

Bad gussets:

- decorative fins
- too thin to print
- blocking screwdrivers or wires
- making the part ugly without improving load path

---

## Boss Design

Bosses should not be isolated cylinders unless the load is very small.

A good boss includes:

- correct hole diameter
- adequate outside diameter
- enough screw or insert depth
- broad base pad
- ribs or gussets tying into the floor/wall
- chamfer or lead-in when useful
- enough clearance for tools and screw heads

For every boss, define:

- screw size
- hole type: clearance, pilot, threaded insert, or self-tapping
- boss outer diameter
- boss height
- wall thickness around the hole
- whether reinforcement ribs are needed

Avoid:

- bosses too close to edges
- tall skinny bosses
- bosses with no base support
- bosses that split during insert installation
- bosses that block assembly

---

## Heat-Set Insert Boss Design

Heat-set inserts require geometry that resists splitting, pull-out, and heat distortion.

Guidelines:

- use manufacturer-recommended pilot diameter when available
- parameterize insert hole diameter
- parameterize insert depth
- leave enough wall thickness around insert
- avoid placing inserts near unsupported edges
- add a base pad under the boss
- add ribs/gussets into the floor or wall
- leave vertical access for soldering iron installation
- add top chamfer/lead-in if useful
- test actual insert fit in a printed coupon

Do not guess final insert dimensions. If actual insert specs are unknown, make the insert dimensions parameters and document the assumption.

---

## Fillets, Chamfers, and Stress Transitions

Sharp internal corners concentrate stress.

Use fillets, chamfers, or rounded transitions at:

- mounting ears
- boss bases
- wall-to-floor intersections
- rib bases
- grommet openings
- cable saddle edges
- connector cutouts
- snap or clip roots

In OpenSCAD, true fillets can be expensive. Use practical alternatives:

- rounded rectangles
- hull-based rounded shapes
- chamfers
- cylinders blended into rectangular forms
- simplified radiused lugs

Avoid sharp inside corners where the part will flex or vibrate.

---

## Wall Thickness

Keep wall thickness consistent where practical.

For 3D printing:

- low-load wall: 2.0 mm minimum
- normal functional wall: 2.5 mm to 3.0 mm
- rugged electronics wall: 3.0 mm to 4.0 mm
- rugged floor/base: 3.0 mm to 5.0 mm

For injection molding:

- avoid abrupt thick-to-thin transitions
- avoid large solid masses
- core out thick areas
- use ribs instead of huge blocks
- consider sink marks around bosses
- consider draft angles
- maintain consistent wall thickness where possible

Do not make everything thick just because strength is needed. Use structure first.

---

## 3D Printing Design Rules

Design parts for real printing, not just rendering.

Consider:

- print orientation
- layer-line weakness
- nozzle diameter
- wall count
- infill
- overhangs
- bridging
- support removal
- heat-set insert access
- screw direction relative to layer lines
- tolerance stackup

Avoid:

- tiny slots that will close up
- thin towers
- long unsupported bridges
- flat tabs loaded across layer lines
- screw bosses that split along layers
- unsupported overhangs over 45 degrees unless acceptable
- decorative details too small to print

Preferred clearances:

- general FDM fit clearance: 0.3 mm to 0.6 mm
- PCB pocket clearance: 0.5 mm to 0.75 mm per side
- lid or sliding fit clearance: 0.3 mm to 0.5 mm per side
- zip-tie tunnel clearance: actual zip-tie size plus print tolerance
- grommet/cable gland hole: based on actual hardware datasheet

Material guidance:

- PLA: prototypes only; not preferred for heat, vehicle, or outdoor use
- PETG: good general toughness and easier printing
- ASA: better UV and outdoor resistance
- ABS: better heat resistance but harder to print
- Nylon: strong and tough, but requires dry filament and correct setup
- TPU: useful for seals, bumpers, grommets, and vibration isolation

---

## Injection Molding Design Rules

If a part may later be injection molded, design with future molding in mind.

Consider:

- draft angles
- consistent wall thickness
- rib thickness
- cored bosses
- sink marks
- parting line
- ejector pin access
- undercuts
- mold shutoffs
- radiused corners
- material shrinkage

Avoid:

- trapped geometry
- unnecessary undercuts
- huge solid blocks
- vertical walls with no draft
- very thick bosses with no coring
- thin fragile fins
- complex internal tunnels that cannot be molded

If a feature is acceptable for 3D printing but bad for injection molding, document that tradeoff.

---

## Electronics Enclosure Rules

For electronics housings, always account for:

- PCB length and width
- PCB thickness
- mounting hole coordinates
- mounting screw size
- component height
- bottom solder joint clearance
- connector access
- wire bend radius
- wire strain relief
- heat-set insert access
- grommet or cable gland entry
- service access
- lid clearance
- sealing strategy
- water/dust paths
- vibration and shock
- future board revisions

Do not create:

- random wall gaps
- exterior zip-tie holes if sealing matters
- connector holes without clearance
- unreinforced standoffs
- unserviceable screw locations
- wire paths that cannot physically be assembled
- walls that block soldering or screw access

Exterior wall openings must be intentional.

For dust/water resistance:

- use one deliberate grommet or cable-gland entry where practical
- keep exterior walls solid
- avoid unnecessary holes
- reinforce grommet openings
- keep zip-tie features internal-only
- do not create hidden leak paths

---

## Wire Management and Strain Relief

Wire management is structural, not cosmetic.

Wires must not transfer vibration directly into solder joints.

Use:

- internal cable-tie saddle mounts
- molded bridge tunnels
- floor-mounted zip-tie bases
- wall-integrated internal anchors
- wire routing channels
- grommeted entries
- cable gland zones
- bend-radius space

Do not use:

- random blocks
- tall unsupported zip-tie towers
- through-wall zip-tie holes when sealing matters
- tiny unusable slots
- sharp wire bends
- anchors that block PCB installation

Cable-tie saddles should have:

- low-profile base
- rounded rails
- real tunnel for zip tie
- enough slot/tunnel clearance
- reinforced base
- no exterior leak path
- serviceable placement

---

## Mounting Tabs, Ears, and Brackets

External mounting points must be clean, strong, and intentional.

Avoid:

- flat unsupported ears
- ugly fork shapes
- random fin farms
- thin cantilever tabs
- screw holes close to edges
- sharp inside corners
- mount geometry that looks like patched-on junk

Preferred:

- rounded rectangular ears
- oval or teardrop mounting lugs
- raised boss around screw hole
- wide neck into enclosure body
- smooth blend into wall/floor
- underside gussets
- clean diagonal ribs if needed
- compact automotive-style geometry

For off-road or vehicle use:

- design for vibration
- design for shock
- use strong wall/floor load paths
- reinforce screw holes
- avoid thin tabs
- avoid brittle geometry
- use radiused transitions

---

## Serviceability Rules

A part is not finished unless it can be assembled and serviced.

Check:

- Can the PCB drop in?
- Can screws be installed?
- Can a screwdriver reach the screws?
- Can heat-set inserts be installed?
- Can wires be soldered?
- Can zip ties be threaded and tightened?
- Can wires bend naturally?
- Can connectors plug and unplug?
- Can the lid be removed?
- Can the part be printed without impossible supports?
- Can damaged wiring or hardware be replaced?

Never block access to:

- screws
- solder pads
- connectors
- programming headers
- reset buttons
- fuses
- grommets
- cable ties
- fasteners

---

## OpenSCAD Design Rules

OpenSCAD code must be clean, modular, and parameterized.

Required:

- major parameters at the top
- named modules
- clear coordinate system comments
- source dimensions separated from design assumptions
- preview helpers separate from production geometry
- no hard-coded critical dimensions hidden deep in modules
- rejected geometry removed or clearly disabled
- renderable code
- simple geometry unless complexity is justified

Preferred module names:

- `base_body()`
- `perimeter_walls()`
- `pcb_standoffs()`
- `heat_set_insert_boss()`
- `mounting_boss()`
- `rounded_mount_ear()`
- `triangular_gusset()`
- `diagonal_rib()`
- `reinforcement_ribs()`
- `wire_entry()`
- `grommet_entry()`
- `cable_tie_saddle()`
- `board_guides()`
- `service_clearance_features()`
- `preview_part()`
- `main_assembly()`

When modifying OpenSCAD:

- read the whole file first
- preserve good working parameters
- remove rejected features instead of hiding them under more geometry
- refactor bad modules instead of stacking patches
- avoid fragile boolean operations
- test render if possible
- document major parameters in project notes

---

## Design Review Checklist

Before saying a design is complete, verify:

1. Does it match the latest user feedback?
2. Are rejected features fully removed?
3. Are dimensions based on source facts?
4. Are assumptions labeled?
5. Are loads carried through real load paths?
6. Are bosses reinforced?
7. Are tabs/ears supported?
8. Are ribs/gussets functional, not decorative?
9. Are exterior openings intentional?
10. Are wire strain-relief features usable?
11. Does it avoid leak paths when water/dust resistance matters?
12. Can it be printed?
13. Can it be assembled?
14. Can it be serviced?
15. Does it look clean and intentional?
16. Is it compact without being weak?
17. Are key dimensions parameterized?
18. Was the project memory updated?

---

## Final Strength Rule

Do not solve strength by only making everything thicker.

First improve:

- load paths
- ribs
- gussets
- triangular bracing
- boss support
- wall-to-floor transitions
- fillets and chamfers
- print orientation
- service clearance

Use material only where it helps the structure.

---

## CAD Tool Selection Standards

Verify the exact target path before changing source CAD, exports, project memory, or training material. The CAD root is:

```text
C:\Users\LJ\CAD Projects
```

Use OpenSCAD for:

- parametric mechanical parts
- enclosures
- holes and repeated hole patterns
- ribs and gussets
- brackets and bosses
- PCB carriers
- production STL from code-driven geometry

OpenSCAD must keep production and preview geometry separated. Export STL using production mode only. Do not force organic surface modeling into OpenSCAD when the result should be a FreeCAD or mesh-reference workflow.

Use FreeCAD for:

- STEP/solid CAD
- sketches and constraints
- fillets and chamfers
- surface modeling support
- assemblies
- imported STEP/STL reference inspection
- macro-driven solid CAD automation

FreeCAD 1.1 path:

```text
C:\Program Files\FreeCAD 1.1\bin
```

Hybrid rule:

- Use OpenSCAD for parametric/code-driven mechanical systems.
- Use FreeCAD for parts needing fillets, STEP output, sketches, constraints, or better organic/surface control.
- Use imported STL/mesh reference when recreating complex organic parts.

Shared reusable code belongs under `Shared Modules`. Generated exports belong in project-local exports and optionally root `Exports`.
