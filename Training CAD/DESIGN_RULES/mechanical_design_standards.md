# Mechanical Design Standards

Do not create weak hobby-grade geometry unless the part is clearly low-load.

Always design like a mechanical product designer.

## Core Mindset

Every part should be:

- Strong enough for its real environment.
- Printable or manufacturable.
- Serviceable.
- Compact where possible.
- Clean and intentional.
- Parameterized when coded.
- Based on real dimensions.
- Documented when assumptions are made.

Avoid random blocks, weak flat plates, unsupported posts, thin cantilever tabs, decorative ribs, oversized bulk, unnecessary exterior holes, and geometry that only looks good in a render.

## Load Paths

Every structural feature must have a clear path for force to travel into the stronger body of the part.

Fastener loads should flow into bosses, ribs, walls, floors, reinforced corners, or broad mounting necks.

Wire strain should flow into internal strain relief, cable saddles, zip-tie anchors, wire channels, grommets, or cable glands.

Shock and vibration loads should not be carried by thin tabs, isolated bosses, sharp internal corners, or tall unsupported posts.

## Ribs, Gussets, Trusses, And Lattices

Use triangular load paths when vibration, shock, or bending is expected.

Use ribs and gussets to connect real load-bearing features. If a rib does not transfer force, stiffen a weak area, or protect against bending/twisting, remove it.

Do not use decorative fin farms or lattices that add print complexity without structural value.

## Boss Design

Bosses should not be isolated cylinders unless the load is very small.

A good boss includes:

- Correct hole diameter.
- Adequate outside diameter.
- Enough screw or insert depth.
- Broad base pad.
- Ribs or gussets into the floor or wall.
- Tool access.
- Chamfer or lead-in where useful.

## Heat-Set Inserts

Heat-set insert bosses should resist splitting, pull-out, and heat distortion.

Parameterize insert hole diameter and insert depth. Use actual insert data when available. Add base pads, ribs, and enough surrounding wall thickness.

## Fillets And Chamfers

Use rounded or chamfered transitions at mounting ears, boss bases, wall-to-floor joints, rib bases, grommet openings, cable saddle edges, and connector cutouts.

OpenSCAD fillets can be expensive. Practical rounded rectangles, hulls, and chamfers are acceptable.

## Wall Thickness

Use consistent wall thickness where practical.

Typical FDM guidance:

- Low-load wall: 2.0 mm minimum.
- Functional wall: 2.5 mm to 3.0 mm.
- Rugged electronics wall: 3.0 mm to 4.0 mm.
- Rugged floor/base: 3.0 mm to 5.0 mm.

Do not solve strength by only making everything thicker. Improve load paths, ribs, gussets, boss support, wall-to-floor transitions, fillets, print orientation, and service clearance first.

## Enclosure Rules

Electronics enclosures must account for PCB dimensions, board thickness, component height, solder joint clearance, connector access, wire bend radius, heat-set inserts, screw access, grommet/cable gland entry, water/dust paths, vibration, and future board revisions.

Exterior wall openings must be intentional. If water or dust resistance matters, keep zip-tie features internal-only and use a deliberate grommet or cable gland for wire entry.

## Wire Management

Wire strain must not load solder joints.

Preferred features:

- Internal cable-tie saddles.
- Molded bridge tunnels.
- Floor-mounted zip-tie bases.
- Internal wall-integrated anchors.
- Wire routing channels.
- Grommeted entries.

Avoid random blocks, tall unsupported towers, through-wall zip-tie holes, tiny unusable slots, and sharp wire bends.

## Mounting Tabs And Brackets

External mounting points should be clean, strong, and intentional.

Prefer rounded rectangular ears, oval lugs, raised bosses, wide necks, smooth load paths, and clean gussets.

Avoid flat unsupported ears, ugly fork shapes, random fin farms, thin cantilever tabs, screw holes close to edges, and sharp inside corners.

