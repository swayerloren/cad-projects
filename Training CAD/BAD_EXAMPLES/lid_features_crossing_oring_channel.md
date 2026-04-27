# Bad Example: Lid Features Crossing O-ring Channel

Do not place relay bosses, ribs, clamp previews, labels, or other underside
features across an O-ring groove or sealing land.

Failure pattern:

- The lid has a groove, but underside features are allowed to overlap it.
- The base/lid fit is judged from a general render instead of a seal keepout
  view.
- The lid cannot be trusted to seat or seal because the channel is not treated
  as a hard no-go zone.

Corrective rule:

- Define a perimeter seal keepout.
- Clip underside features away from the keepout in production geometry.
- Render closed, cutaway, underside, and seal-keepout views after fresh STL
  export.
