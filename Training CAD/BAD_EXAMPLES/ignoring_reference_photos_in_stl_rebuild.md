# Bad Example: Ignoring Reference Photos In STL Rebuild

Failure pattern:

- the model matches STL bounding boxes but ignores product photos
- styled details are replaced with generic blocks
- part color separation is lost
- holes/openings and user-facing features are approximate or missing
- functional placeholders are not tested against the photo-visible use case

Why it fails:

Styled products are judged by silhouette, proportions, visual language, and function. A rebuild can be dimensionally close but still look like the wrong object.

Corrective rule:

When photos are available, create a photo review and use it to check:

- product identity
- silhouette
- color/material part separation
- functional contact points
- visible fastener and support features
- what cannot be confirmed

Do not claim visual accuracy if the model has only been checked against bounding boxes.
