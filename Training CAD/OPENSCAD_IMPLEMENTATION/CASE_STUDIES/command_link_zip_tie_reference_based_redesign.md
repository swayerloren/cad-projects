# Case Study: COMMAND LINK Zip-Tie Reference-Based Redesign

The COMMAND LINK enclosure originally evolved through several cable tie concepts. A six-per-side wall bridge layout was functional on paper, but the visible result looked like a ladder/rack/grille.

The reference folder `ZIP TIE DESIGN IDEA` clarified the target:

- individual clips
- four per long side by default
- upper and lower rounded slots
- solid center bridge
- no exterior wall cut
- no continuous rack panel

Implementation response:

- added `wall_tie_clip_body()`
- added `wall_tie_slot_cuts()`
- added `wall_tie_clip()`
- added `wall_tie_clip_layout()`
- defaulted `wall_tie_count_per_side` to `4`
- retained optional six-per-side mode only through parameters
- kept old rack behind `show_old_zip_tie_rack = false`

Lesson:

Reference images can invalidate an otherwise functional CAD solution. If the design target is an individual molded clip, a dense rack is wrong even if the slots technically work.
