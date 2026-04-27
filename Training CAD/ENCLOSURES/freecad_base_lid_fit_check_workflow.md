# FreeCAD Base/Lid Fit Check Workflow

Use FreeCAD for enclosure fit checks when base/lid seating, O-ring grooves, heat-set inserts, screw alignment, and STEP export matter.

## Minimum Checks

- Lid lip outer size is smaller than the base inner opening by the intended clearance.
- Screw clearance holes align with insert bosses.
- O-ring groove does not get crossed by ribs, bosses, brackets, or relay mounts.
- Cable gland/grommet retaining nut and tool envelope are modeled.
- Relay bracket screws and bodies clear the seal keepout.
- Closed and exploded renders are exported.

## Documentation

Create project-local reports for:

- base/lid fit
- grommet or cable gland clearance
- relay bracket clearance
- export status

Project-specific details belong in `CODEX\PROJECTS`. Reusable fit-check patterns belong in `Training CAD`.

