# Bad Example: Bounding-Box-Only STL Rebuild

## Problem

Matching only X/Y/Z dimensions can produce a model that is technically close but visually and functionally wrong.

Common failures:
- flat boards replace curved shells
- random tube lines replace intentional frames
- decorative text and panel seams disappear
- lips, slots, and user contact features become unclear
- no real object placeholder verifies use

## Rule

Do not accept a styled or ergonomic rebuild just because the bounding boxes are close.

Require:
- overlay render
- side-by-side render
- visual review table
- functional placeholder check
- list of style features intentionally simplified
