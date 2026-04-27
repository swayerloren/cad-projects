# Hard Lid Seal Keepout Zone

Sealed enclosures need a hard no-go zone around the O-ring groove and base-wall
seating path.

Implementation guidance:

- Define the keepout as a parameter, not a visual guess.
- Use the keepout to subtract or clip underside ribs, bosses, and bracket
  features.
- Show the keepout in preview mode as translucent red geometry.
- Keep production geometry clear; do not rely only on color or documentation.

Minimum checks:

- O-ring groove is unobstructed.
- Base sealing land aligns with the groove.
- Lid lip clears the base wall.
- Fastener holes and relay bosses do not create unplanned leak paths.
