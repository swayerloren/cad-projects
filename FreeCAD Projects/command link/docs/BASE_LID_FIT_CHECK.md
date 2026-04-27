# COMMAND LINK Base/Lid Fit Check

Date: 2026-04-27

## Checked Dimensions

- Body width: `93.50 mm`
- Body length: `98.71 mm`
- Wall thickness: `3.50 mm`
- Base total wall/floor/rim height: `24.90 mm`
- Base sealing land height: `0.80 mm`
- Lid vertical seating clearance: `0.35 mm`
- Lid sealing lip clearance: `0.35 mm`
- Lid screw clearance diameter: `3.40 mm`
- Base insert pilot diameter: `4.20 mm`

## Scripted Checks

Result from `macros\fit_check_base_lid.py`:

```text
lid_seats_on_base: PASS
screw_holes_align: PASS
grommet_tool_clearance: PASS
relay_bracket_screws_clear_seal: PASS
```

## Status

PASS for CAD-level base/lid seating and screw alignment.

Manual checks still required:

- printed lid seating
- O-ring compression
- screw sealing strategy
- final heat-set insert fit

