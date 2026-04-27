# Before/After Review: STL Rebuild Visual Accuracy

## Bad Pattern

A rebuild can match STL bounding boxes and still fail.

Bad signs:
- silhouette does not match the original
- styled surfaces are reduced to random blocks or straight tubes
- functional use case is not tested with a placeholder
- overlays are generated but not reviewed by category
- documentation says "close" because dimensions match, while the object looks wrong

This happened in the racing seat phone stand rebuild: the first version matched broad envelopes but did not capture the racing seat style, rollcage shape, base styling, or phone stand function well enough.

## Good Pattern

A better STL rebuild includes:
- visual accuracy review by category
- side-by-side original and rebuild renders
- translucent overlay renders
- silhouette/proportion comparison
- functional placeholder testing
- documentation of remaining style limits

For styled parts, success is not only dimensional. It must also preserve design intent.
