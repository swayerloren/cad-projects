# Global Codex Instructions

These instructions apply to all CAD, OpenSCAD, enclosure, mechanical design, 3D printing, CNC, and injection-molding projects tracked in this knowledge repository.

This `CODEX` folder is for knowledge, project memory, standards, errors, decisions, and prompts. Actual CAD project source files stay in their own source folders unless a task explicitly says otherwise.

CODEX is project memory. Training CAD is clean reusable learning material for local AI/LLM retrieval and future training across OpenSCAD, FreeCAD, and general CAD work.

The CAD root is:

```text
C:\Users\LJ\CAD Projects
```

---

## 1. Required Workflow Before Any Edit

Before editing any CAD, OpenSCAD, STEP, STL, KiCad, enclosure, or mechanical source file:

1. Identify the exact target project.
2. Identify the exact source folder.
3. Read the project-specific knowledge files first:
   - `FACTS.md`
   - `INSTRUCTIONS.md`
   - `DESIGN_DECISIONS.md`
   - `ERRORS_AND_FIXES.md`
   - `DO_AND_DONT.md`
   - `OPENSCAD_PARAMETERS.md` if present
   - latest files in `OUTPUT_REVIEWS/` if present
4. Read the current source CAD/code file before modifying it.
5. Preserve working features unless the user explicitly rejected them.
6. Do not modify unrelated files.
7. Separate confirmed facts from assumptions.
8. Do not guess dimensions when source files can be inspected.
9. Keep changes small, testable, and documented.
10. After major design changes, update the project knowledge files.

---

## 2. Mechanical Design Mindset

Do not generate weak hobby-grade parts unless the task is clearly low-load.

Always design like a mechanical product designer.

Every part should consider:

- real load paths
- assembly process
- serviceability
- manufacturing method
- print orientation
- material behavior
- screw/insert loads
- vibration/shock
- wire strain relief
- tolerances
- long-term durability
- clean professional appearance

Default visual target:

- clean
- OEM-like
- rugged when needed
- compact
- manufacturable
- parameterized
- not overcomplicated
- not random blocks
- not decorative geometry pretending to be structure

---

## 3. Strength Design Rules

Do not solve strength by only making everything thicker.

First improve:

- load paths
- ribs
- gussets
- triangular bracing
- boss support
- wall-to-floor transitions
- fillets/chamfers
- print orientation
- service clearance
- fastener load distribution

Use material only where it helps the structure.

### Always ask before finalizing a part:

1. Where does the force enter?
2. Where does the force exit?
3. What bends first?
4. What twists first?
5. What breaks if the screw is overtightened?
6. What fails under vibration?
7. What fails along layer lines?
8. Can this be assembled?
9. Can this be serviced?
10. Is the geometry strong for a reason, or just bulky?

---

## 4. Load Paths

Every mounting feature, bracket, tab, standoff, boss, clip, latch, hinge, or zip-tie anchor must have a visible load path into the main body.

Bad:
- flat ears sticking out from a wall
- tall unsupported posts
- screw bosses standing alone
- zip-tie towers with no base support
- thin tabs with sharp inside corners

Good:
- boss tied into wall/floor with ribs
- rounded mount ears with wide necks
- triangular gussets at high-load transitions
- reinforced corners
- diagonal ribs from fastener boss to main body
- smooth transitions from thin to thick areas

---

## 5. Ribs, Gussets, Trusses, and Lattices

Use structural reinforcement intentionally.

### Reinforcing ribs
Use ribs to stiffen flat plates, walls, mounting tabs, brackets, and bosses.

Ribs should:
- connect real structural features
- follow load paths
- reduce flex
- avoid blocking assembly
- avoid unnecessary bulk

### Gussets
Use triangular gussets where vertical and horizontal features meet.

Use gussets around:
- PCB standoffs
- heat-set insert bosses
- mounting ears
- cable-tie anchors
- wall-to-floor transitions
- brackets
- tabs
- connector supports

### Truss design
Use triangles and diagonal members to resist bending and twisting.

Use truss-style reinforcement when:
- a mount sticks out from the body
- a tab may flex
- the part needs strength without becoming solid
- vibration or shock is expected

### Lattice structures
Use lattice/web structures only when they make manufacturing and structural sense.

Do not create decorative lattice that:
- adds print complexity without strength
- traps dirt/water
- is too thin to print reliably
- blocks access
- makes injection molding impossible

---

## 6. Bosses, Screws, and Heat-Set Inserts

Screw bosses and insert bosses must be engineered, not just cylinders.

For every boss:
- define screw size
- define clearance hole or insert hole
- define boss outer diameter
- define boss height
- define insert depth if using inserts
- leave enough wall thickness around the insert
- add ribs/gussets connecting the boss to the floor/wall
- leave tool access for a screwdriver
- avoid placing bosses too close to edges unless reinforced

For heat-set inserts:
- parameterize insert hole diameter
- parameterize insert depth
- include enough surrounding material to prevent splitting
- avoid bottoming out the insert unless designed intentionally
- leave a lead-in/chamfer when practical
- never assume insert dimensions; record actual insert specs when known

---

## 7. 3D Printing Rules

Design for real 3D printing, not just screen rendering.

Consider:
- print orientation
- layer strength
- overhangs
- bridges
- support removal
- nozzle size
- wall count
- infill direction
- tolerance stackup
- heat resistance
- vibration resistance

Avoid:
- thin vertical towers
- weak layer-peel tabs
- unsupported long bridges
- tiny slots that close up during printing
- decorative detail smaller than practical nozzle resolution
- sharp internal corners at stress points

Preferred 3D printing defaults unless project says otherwise:
- minimum wall thickness: 2.0 mm
- rugged wall thickness: 3.0–4.0 mm
- floor thickness for rugged electronics: 3.0–5.0 mm
- practical clearance between printed parts: 0.3–0.6 mm
- PCB pocket clearance: 0.5–0.75 mm per side
- zip-tie slot clearance: real zip tie size plus tolerance
- screw clearance holes: actual screw clearance, not nominal screw diameter

Material awareness:
- PLA is not preferred for vehicle, outdoor, heat, or vibration use.
- PETG is better for general toughness.
- ASA or ABS is better for heat and outdoor exposure.
- Nylon or fiber-filled nylon may be better for rugged brackets, but requires correct printing setup.
- TPU is useful for vibration isolation, grommets, bumpers, and flexible strain relief.

---

## 8. Injection Molding Awareness

If a part may later be injection molded, avoid 3D-print-only habits that would create molding problems.

Consider:
- draft angles
- consistent wall thickness
- ribs instead of thick solid blocks
- avoiding sink marks
- avoiding trapped undercuts
- avoiding impossible shutoffs
- mold parting direction
- ejector access
- rounded internal corners
- boss coring
- proper rib thickness

General rule:
- For injection molding, ribs are often about 40%–70% of nominal wall thickness.
- Avoid large solid masses.
- Use cored bosses and supported ribs.
- Add draft where vertical walls would be molded.
- If a design is only for 3D printing right now, note what would need to change for molding.

---

## 9. Enclosures and Electronics Housings

For electronics enclosures, always consider:

- PCB dimensions
- board thickness
- component height
- solder joint clearance
- connector clearance
- wire bend radius
- heat-set inserts
- screw access
- service access
- wire strain relief
- grommet/cable gland entry
- water/dust paths
- vibration
- standoff support
- lid/seal strategy
- future board revisions

Do not create:
- random wall gaps
- zip-tie holes through exterior walls unless intentionally acceptable
- connector openings without clearance
- standoffs with no reinforcement
- unserviceable screw locations
- wire paths that cannot physically be assembled

For exterior walls:
- keep them solid unless the opening is intentional
- use circular grommet holes or cable gland features for wire entry when water/dust resistance matters
- reinforce openings with bosses/rings
- avoid unnecessary leak paths

---

## 10. Wire Management and Strain Relief

Wire management features must be usable in real life.

For zip ties:
- slots must fit actual zip ties
- tunnel height must account for print tolerance
- tie path must be physically possible
- avoid slots that cut through exterior walls if water/dust resistance matters
- avoid tiny decorative slots
- avoid weak standalone posts

Preferred features:
- internal cable-tie saddle mounts
- molded bridge tunnels
- internal wall-integrated strain relief
- floor-mounted saddle bases
- rounded rails
- reinforced lugs
- grommeted wire entry
- cable gland zones

Do not:
- make random blocks
- make tall unsupported zip-tie towers
- create leak paths through enclosure walls
- block PCB installation or solder access
- force wires into sharp bends

---

## 11. Mounting Tabs, Ears, and Brackets

External mounting points must be clean and strong.

Avoid:
- flat unsupported ears
- ugly fork shapes
- random fin farms
- thin cantilevered tabs
- sharp inside corners
- screw holes too close to edges

Preferred:
- rounded rectangular ears
- oval/teardrop mounting lugs
- raised boss/ring around fastener hole
- wide neck into the enclosure body
- clean underside gussets
- smooth wall/floor load path
- compact automotive-style geometry

For off-road, vehicle, marine, or equipment use:
- design for vibration and shock
- use generous radii/chamfers
- reinforce screw bosses
- use gussets where the tab meets the body
- make mounts look molded and intentional

---

## 12. Serviceability Rules

A part is not finished unless it can be assembled and serviced.

Check:
- Can the PCB drop in?
- Can screws be installed with a normal driver?
- Can heat-set inserts be installed?
- Can wires be soldered?
- Can zip ties be threaded?
- Can wires bend without being crushed?
- Can connectors plug/unplug?
- Can the lid be removed?
- Can the part be printed without impossible supports?
- Can failed parts be replaced?

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

## 13. OpenSCAD Code Standards

OpenSCAD files must be clean, editable, and parameterized.

Required practices:
- place major parameters at the top
- use meaningful module names
- avoid hard-coded critical dimensions deep inside modules
- comment coordinate systems
- comment design intent
- keep preview helpers separate from production geometry
- make rejected features removed or disabled clearly
- avoid fragile geometry that fails to render
- avoid overly complex boolean operations when simpler geometry works

Preferred module naming:
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

When changing an existing SCAD file:
- preserve good parameters
- remove rejected geometry
- do not stack patches on top of bad design
- refactor bad modules instead of adding more junk
- keep the file renderable

---

## 14. Design Review Before Final Response

Before saying a CAD change is complete, review it against the latest user feedback.

Check for:
- rejected features still present
- ugly geometry
- random blocks
- weak tabs
- exterior leak paths
- impossible wire routing
- blocked screw access
- missing reinforcement
- too much wasted space
- unparameterized dimensions
- mismatch with project facts

If the latest user rejected a feature, do not preserve it.

---

## 15. Documentation and Memory

After major changes, update the relevant project knowledge files:

- `CHANGELOG.md`
- `ERRORS_AND_FIXES.md`
- `DESIGN_DECISIONS.md`
- `DO_AND_DONT.md`
- `OPENSCAD_PARAMETERS.md`
- `OUTPUT_REVIEWS/`

Record:
- what changed
- why it changed
- what was rejected
- what must not be repeated
- what parameters matter
- what source facts were used

Do not let the same mistake repeat across prompts.

---

## 16. Final Response Rules for Codex

When finished, report only:

- files created or updated
- source files read
- key changes made
- rejected features removed
- new parameters added
- any limitations or assumptions
- whether the file renders successfully if tested

Do not write long explanations unless requested.
Do not claim a design is rugged unless it actually has load paths, ribs/gussets, and serviceable geometry.

---

## STL Rebuild Quality Requirement

When rebuilding STL projects into OpenSCAD, Codex must not rely only on bounding-box matching.

Codex must verify:
- silhouette accuracy
- major feature placement
- hole locations
- part function
- assembly fit
- visual proportions
- serviceability
- mechanical relationships
- original-to-rebuild overlay
- functional placeholder testing where relevant

For styled parts, Codex must check:
- overall design language
- curves/silhouette
- proportions
- visual style
- user-facing function

For mechanical assemblies, Codex must check:
- axes
- center distances
- gear/pulley/bearing relationships
- rotation clearance
- stack height
- fastener alignment
- motion/function path

Every STL rebuild project must include either:
- `VISUAL_ACCURACY_REVIEW.md` for styled/static parts, or
- `MECHANICAL_ACCURACY_REVIEW.md` for mechanical assemblies.

Bounding-box match alone is not acceptable.

If the rebuild is intentionally simplified, Codex must clearly mark what is simplified and why, and it must not claim the model is accurate beyond what was actually verified.

---

## Training Repository Maintenance

The training repo is:

```text
C:\Users\LJ\CAD Projects\Training CAD
```

Before finishing any CAD/OpenSCAD/mechanical design task, Codex must consider whether the task produced reusable knowledge.

If reusable knowledge was produced, Codex should update the Training CAD repo with:

- good examples
- bad examples
- before/after reviews
- reusable OpenSCAD modules
- reusable FreeCAD macros or workbench notes
- design rules
- hybrid CAD workflow notes
- STL reverse-engineering notes
- surface-modeling notes
- prompt templates
- JSONL Q/A or design pattern records

Codex must keep Training CAD clean and reusable, not dump messy raw logs.

Codex should not store secrets, tokens, personal information, or irrelevant raw files in Training CAD.

Codex should update `TRAINING_INDEX.md` when adding new training material.

Codex should keep project-specific messy working memory in CODEX, and clean generalized learning material in Training CAD.

Codex should create new topic folders when a new repeated design area appears, such as:

- hinges
- snap fits
- gasket channels
- cable glands
- relay board carriers
- waterproof seals
- vibration isolation
- automotive brackets
- PCB stackups

Codex should record source project references without copying unnecessary private files.

## OpenSCAD Implementation Documentation Requirement

When a Codex task creates or fixes OpenSCAD geometry, Codex must document not only the mechanical design intent, but also the OpenSCAD implementation method when useful.

This includes:

- modules created or changed
- key parameters
- coordinate mapping
- boolean cut logic
- tunnel, slot, and cutout strategy
- preview/debug helpers
- render/test notes
- known OpenSCAD failure modes avoided
- serviceability validation

If the implementation lesson is reusable, Codex must add it to:

```text
C:\Users\LJ\CAD Projects\Training CAD\OPENSCAD_IMPLEMENTATION
```

---

## CAD Root Architecture Rules

1. Verify the exact target path before reading, editing, moving, exporting, or documenting CAD work.
2. The CAD root is `C:\Users\LJ\CAD Projects`.
3. `CODEX` stores project memory, instructions, facts, design decisions, errors, paths, and project-specific notes.
4. `Training CAD` stores reusable lessons across OpenSCAD, FreeCAD, general CAD, manufacturing, STL reverse engineering, and future AI/local LLM training data.
5. OpenSCAD projects go under `OpenSCAD Projects` unless the user says otherwise.
6. FreeCAD projects go under `FreeCAD Projects` unless the user says otherwise.
7. Shared reusable code goes under `Shared Modules`.
8. Generated exports go under project-local `exports` folders and optionally root `Exports`.
9. Never silently edit similarly named folders.
10. Before the final response, verify the exact files modified.

## OpenSCAD Workflow

OpenSCAD is best for parametric mechanical parts, enclosures, holes, ribs, brackets, bosses, PCB carriers, and repeatable code-driven geometry.

OpenSCAD rules:

- Use production/preview mode separation.
- Export STL using production mode.
- Keep preview and debug helpers out of exported production STL.
- Avoid organic surface modeling when OpenSCAD is not appropriate.
- Store reusable modules in `Shared Modules\OpenSCAD` when they are stable enough to share.

## FreeCAD Workflow

FreeCAD is best for STEP/solid CAD, sketches, constraints, fillets/chamfers, surface modeling support, assemblies, and work that benefits from a CAD feature tree.

FreeCAD path:

```text
C:\Program Files\FreeCAD 1.1\bin
```

Store reusable FreeCAD macros and modules in:

```text
C:\Users\LJ\CAD Projects\Shared Modules\FreeCAD
C:\Users\LJ\CAD Projects\tools\FreeCAD Macros
```

Use FreeCAD Python macros when they make modeling, export, measurement, or validation repeatable.

## Hybrid CAD Rule

- Use OpenSCAD for parametric/code-driven mechanical systems.
- Use FreeCAD for parts needing fillets, STEP output, sketches, constraints, assemblies, or better organic/surface control.
- Use imported STL/mesh reference when recreating complex organic parts.

---

## Exact Active Path Rule

Codex must verify the exact user-provided active file exists before editing. If multiple similarly named project folders exist, Codex must report them and must not silently edit the wrong one.

Before any source edit:

1. Confirm the current root is `C:\Users\LJ\CAD Projects`.
2. Confirm the active project folder.
3. Confirm the exact source file path.
4. Confirm the exact export path.
5. Read project `PATHS.md` when present.

If old notes reference `C:\Users\LJ\OpenSCAD Projects`, treat that as historical until the matching current path under `C:\Users\LJ\CAD Projects` is verified.

## Project Memory Rule

Every project must have a CODEX project folder with:

- `PATHS.md`
- `LIVE_WORKING_MEMORY.md`
- `SESSION_HISTORY.md`
- `DESIGN_DECISIONS.md`
- `ERRORS_AND_FIXES.md`
- `DO_AND_DONT.md`
- `TODO.md`

Use `LIVE_WORKING_MEMORY.md` for the current active state, current known problem, current work focus, and what not to touch.

Use `SESSION_HISTORY.md` for chronological session notes, prompt summaries, changes made, user corrections, and verification.

## Training CAD Rule

Reusable lessons go to `Training CAD`, not only the project folder.

Project folders may contain messy working memory and project-specific facts. `Training CAD` must contain clean, generalized, reusable lessons, patterns, examples, and future AI/local LLM training material.

## OpenSCAD / FreeCAD Tool Selection Rule

Use OpenSCAD for parametric mechanical geometry.

Use FreeCAD for fillets, STEP solids, sketches, constraints, assemblies, cleaner surface/solid modeling, and macro-driven solid workflows.

Use hybrid workflow for organic STL-derived parts, complex surface references, or projects where OpenSCAD handles repeatable mechanical structure and FreeCAD handles final solid modeling or export.

## Verification Rule

Before success, create or update:

- render/export outputs when the task changes geometry or deliverables
- pass/fail review document when the task requires output validation
- project memory update for meaningful decisions, errors, path changes, parameters, or next steps

Before the final response, verify the exact files modified and required outputs or documentation exist.

## GitHub Repo Safety Rule

Before committing, Codex must check `.gitignore`, staged files, and large files.

Do not commit generated exports, virtual environments, caches, secrets, tokens, private credentials, or unnecessary binaries unless explicitly requested.

The `cad-projects` repo should normally track:

- documentation
- CODEX memory
- Training CAD reusable lessons
- OpenSCAD source files
- FreeCAD source files when reasonably sized
- FreeCAD macros/scripts
- shared modules
- lightweight reference text files

The repo should generally ignore:

- generated STL/STEP/DXF/image exports
- render folders
- Python virtual environments
- build caches
- FreeCAD backup/cache files
- OpenSCAD logs/temp files

FreeCAD and OpenSCAD applications are installed outside the repo and must not be committed.
