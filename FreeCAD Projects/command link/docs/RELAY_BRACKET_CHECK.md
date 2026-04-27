# COMMAND LINK Relay Bracket Check

Date: 2026-04-27

## Modeled Values

- Relay placeholder width: `28.00 mm`
- Relay placeholder depth: `28.00 mm`
- Relay placeholder height: `32.00 mm`
- Relay layout: compact `3+2`
- Bracket screw spacing: `22.00 mm`
- Bracket type: open-bottom top retainer

## Verification

CAD-level checks:

- Relay brackets are open-bottom top retainers, not trays.
- Relay bracket screw positions clear the modeled seal keepout.
- Relay bracket set exports were created as STEP and STL.
- Relay bracket render was exported:
  - `exports\PNG\render_relay_brackets.png`

Overall status: PARTIAL

Reason:

- Actual relay/socket dimensions are still assumptions.
- Final relay capture geometry must be tuned after measuring the selected relay/socket.

