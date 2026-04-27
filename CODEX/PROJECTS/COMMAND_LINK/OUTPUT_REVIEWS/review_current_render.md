# Current Render Review

## Context

Previous versions improved enclosure walls and compactness compared with the first lightweight carrier tray.

## Rejected Issues

- Zip-tie holes through the outside wall were rejected.
- Rectangular side wire opening was rejected.

## Previous Concern

The previous concern was strengthening outside mounting tabs using truss, lattice, rib, and gusset design.

Mounts must survive off-road vibration and shock.

## New Rejections

- Blocky internal zip-tie mounts were rejected.
- External mount tabs/pods were rejected for ugly non-OEM geometry.

## New Direction

- Use clean molded cable-tie saddle mounts for internal wire strain relief.
- Use clean rounded automotive-style external mounting ears with circular bosses, broad necks, and simple gussets.
- Keep strength through clear load paths, but avoid random truss fins, jagged brackets, or stacked rectangular blocks.

## Latest External Mount Correction

- The external mount pass should focus only on the mount ears, not the whole enclosure.
- Use refined oval/teardrop-style ears outside the enclosure body.
- Each ear should have a centered clearance hole, raised boss, wide blended neck, and two clean gussets.
- Avoid crude fork shapes, flat ears, random truss fins, and blocky patched-on geometry.

## Latest Internal Wire-Retention Correction

- The internal zip-tie pass should focus only on the wire strain relief.
- Use low-profile internal cable-tie saddle bridges, not standalone towers or stacked blocks.
- Keep saddles in wall-side wire lanes outside the PCB footprint.
- Zip ties must pass under the saddle bridge and must not cut through the exterior wall.
- Preserve the circular short-side grommet entry and external mount ears.

## Latest Industrial-Design Style Pass

- Style refinements should not move the PCB, standoffs, grommet hole, wire retention, or external mount holes.
- Use a continuous rounded perimeter shell instead of overlapping wall strips.
- Add a subtle molded top rim and stepped grommet boss so the part reads more like an OEM electronics housing.
- Keep softened edges consistent across guides, ribs, lanes, and saddles.
- Do not add ornamental ribs, fake texture, or cosmetic blocks.

## Production Readiness Review

Review file:

```text
C:\Users\LJ\OpenSCAD Projects\command link\openscad_pcb_carrier\PRODUCTION_REVIEW.md
```

Current readiness:

- Early engineering prototype / pre-production concept.
- Do not call production-ready until hardware and print validation are complete.

Top blockers:

- Actual grommet/cable gland is not selected or validated.
- Heat-set insert pilot/depth must be tested; current insert depth equals standoff height.
- Zip-tie saddle tunnels need physical fit testing with real zip ties.
- Harness bend radius and strain relief need validation with real wire bundle.
- External mount ears need fastener/washer/torque and vibration testing.
- The open-top lower housing has no standalone seal/lid strategy.

Next review focus:

- Print coupons for grommet, insert boss, zip-tie saddle, and external mount ear.
- Confirm PCB fit with real board and soldered wires.
- Define material, print settings, fastener locking, and vibration test plan.

## Latest SCAD Consolidation Pass

- Parameters were organized into PCB facts, enclosure body, PCB standoffs/guides, grommet/wire routing, wire retention, external mounts, and style/preview groups.
- Modules were organized into helper geometry, base/enclosure body, PCB mounting, wire entry, wire retention, external mounts, preview/future placeholders, and main assembly sections.
- Unused or rejected leftovers were removed, including `rounded_rect_2d()`, `mount_ear_layout()`, `wall_corner_radius`, and `mount_ear_corner_radius`.
- The active SCAD should keep only accepted geometry: circular short-side grommet, internal cable-tie saddles, rounded external ears, PCB standoffs, board guides, rugged lower body, and preview helpers.
- Render passed after consolidation.

## Latest Wire-Retention Correction

- The previous internal saddle geometry was rejected because a real zip tie could not clearly pass through it.
- The new requirement is six usable internal cable-tie bridge features per PCB long side, for twelve total retention points.
- Each feature must have a visible rectangular pass-through tunnel under a raised bridge.
- The zip-tie path must be previewed with translucent clearance blocks.
- The exterior wall must remain solid; zip-tie features must not create leak paths.

## Latest Serviceability Correction

- The previous twelve bridge features were rejected because they were too close to the installed PCB and could be trapped by side pad/wire zones.
- The new direction is open-top serviceable cable-tie saddles placed in the channel between PCB edge and inside wall.
- Each side still requires six usable saddles, twelve total.
- Each saddle must be threadable after PCB installation and soldering.
- Preview helpers must show the zip-tie path, wire bundle, and service clearances to PCB and wall.

## Latest Wall-Integrated Zip-Tie Correction

- The floor-mounted saddle concept was rejected because the desired feature is an internal wall-molded bridge slot, not a floor tunnel beside the PCB.
- The new direction is six wall-integrated zip-tie bridge slots on each long inside wall, twelve total.
- Each bridge uses an upper inside-facing slot, a lower inside-facing slot, and a solid center bridge between the slots.
- Slot cutouts must be limited to the inward pad body so the outside enclosure wall remains solid.
- Preview helpers must show the internal tie path and wire bundle without implying any exterior leak path.

## Latest Compact Side-Lane Correction

- The wall-integrated zip-tie bridge concept was accepted, but the first version wasted too much space between the PCB edge and inside wall.
- The side channel must now use a compact service-lane stack: PCB edge, small clearance, wire lane, tie bridge pad, exterior wall.
- Do not make the enclosure overly wide just to make zip-tie access easy.
- The current default side margin is computed from the compact lane stack rather than hard-coded to 26 mm.

## Latest Export / Wall Bridge Refinement

- Preview/helper objects were leaking into production export because helpers were mixed into the main printable assembly.
- The SCAD now has `mode = "preview"`, `mode = "production"`, and `mode = "cutaway"`.
- `production_geometry()` contains only printable enclosure solids.
- `preview_helpers()` contains PCB placeholder, wire markers, zip-tie path previews, wire bundle previews, service clearance markers, and future/debug placeholders.
- Production STL export was tested with `mode="production"` to `exports/command_link_rugged_enclosure_production.stl`.
- Production render shows the enclosure without PCB/wire/zip-tie preview helpers.
- Wall-integrated zip-tie bridges were refined with rounded pad bodies, smoother upper/lower slots, chamfered slot mouths, wider slots, taller center bridge, and local pad blends.
- The continuous wall strip is disabled by default so the six features per side read as individual molded service bridges rather than a hard rail.
- Exterior wall remains solid behind the bridge pads; slot cuts are limited to the inward pad geometry.

## Latest Zip-Tie Mount Audit

- `ZIP_TIE_MOUNT_AUDIT.md` was created for the rugged lower enclosure.
- Count check passed: 6 wall-integrated bridges on the left long wall and 6 on the right long wall.
- Serviceability check passed in preview: PCB placeholder, wire bundle, service clearance, and zip-tie path previews show inside-accessible upper/lower bridge slots.
- Production render check passed: the production render shows no PCB placeholder, wire bundle preview, zip-tie path preview, slot preview, or service-clearance helper solids.
- Production STL export to `exports/command_link_rugged_enclosure_production.stl` completed in `mode="production"`.
- Slot openings are smoother than the previous version because the SCAD now uses named rounded/chamfered slot cutters and a slot-cutout preview toggle.
- Remaining risk: physical print testing is still required with the actual zip tie, wire bundle, PCB, soldered leads, and cutting tool.

## Latest Manufacturing Cleanup Review

- `MANUFACTURING_REVIEW.md` was created for the rugged lower enclosure.
- Production export passed after the cleanup in `mode="production"`.
- Production PNG checked: `exports/command_link_manufacturing_cleanup_production.png`.
- Cleanup reduced boxy transitions at zip-tie pads, external mount bosses, mount gussets, low pads/guides, rim strips, and the grommet boss.
- The cleanup deliberately used fast rounded/chamfered approximations instead of slow true-fillet operations that made export unreliable.
- Grommet hole remains circular, PCB standoff coordinates remain unchanged, and six wall-integrated zip-tie bridges per side remain.
- Remaining risk: this is still an FDM-oriented prototype. Injection molding would need draft, coring, side-core/side-action, wall-thickness, and parting-line redesign.
## Zip-Tie Reference-Based Redesign - 2026-04-26

Active source:

```text
C:\Users\LJ\OpenSCAD Projects\my projects\command link\openscad_pcb_carrier\command_link_rugged_enclosure.scad
```

The previous six-per-side wall-tie design still looked like a ladder/rack/grille. It was replaced in the default render with four individual wall-integrated clips per long side based on the ZIP TIE DESIGN IDEA screenshots and Markdown.

Render checks created:

- `exports/before_zip_tie_redesign_reference_based.png`
- `exports/after_zip_tie_redesign_reference_based.png`
- `exports/after_zip_tie_redesign_left_closeup.png`
- `exports/after_zip_tie_redesign_right_closeup.png`
- `exports/zip_tie_redesign_production_check.png`

Result: visibly changed. The default now shows individual clips, not the long rack. Production mode excludes preview helpers.

## External Mount Redesign - 2026-04-26

Active source:

```text
C:\Users\LJ\OpenSCAD Projects\my projects\command link\openscad_pcb_carrier\command_link_rugged_enclosure.scad
```

The previous external mounts still looked like stacked/layered pods. They were replaced in the default render with four simple integrated teardrop-style mounting ears.

Render checks created:

- `exports/before_external_mounts_full.png`
- `exports/before_external_mounts_closeup.png`
- `exports/after_external_mounts_full.png`
- `exports/after_external_mounts_closeup.png`

Result: visibly changed. The default now uses wide integrated ears with low screw bosses and side gussets. Production STL exported in `mode="production"`.

## Rugged Relay Lid Started - 2026-04-26

New source:

```text
C:\Users\LJ\OpenSCAD Projects\my projects\command link\openscad_pcb_carrier\command_link_rugged_lid.scad
```

Created a separate lid/top-half model with a first-pass O-ring groove, downward sealing lip, six lid fastener holes, and five relay mount zones using ten underside heat-set insert bosses.

Render checks created:

- `exports/lid_preview_full.png`
- `exports/lid_relay_mounts_closeup.png`
- `exports/lid_oring_groove_closeup.png`
- `exports/lid_fastener_bosses_closeup.png`

Production STL:

- `exports/command_link_rugged_lid_production.stl`

Notes: the lower base still needs matching insert bosses and seal landing updates. The relay layout falls back to staggered 3+2 because five 28 mm relay placeholders do not fit in a single row on the compact lid.
