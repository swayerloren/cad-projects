# Bad Example: Gear Machine Rebuild Without Mechanical Accuracy Review

## Failure Pattern

The rebuild matches STL bounding boxes and includes all visible parts, but the mechanism does not make sense.

Common symptoms:
- gear centers are guessed by eye
- connecting gears are placed on separate arbitrary axes
- tooth counts are not checked
- pitch circles are not shown
- center distances are not compared
- vertical stack order is guessed
- cable/tape path is not previewed
- render looks like a pile of parts instead of a machine

## Why This Fails

A gear mechanism is defined by relationships, not just envelopes. If the teeth, pitch circles, shaft axes, and stack order are wrong, the part may look dimensionally close but cannot transmit motion.

## Review Rule

Before accepting any gear-driven STL rebuild, require:
- tooth count estimate
- pitch diameter estimate
- center distance check for each mesh
- axis sharing check for stacked gears
- gear plane/stack order diagram
- original overlay or silhouette comparison
- functional path preview for cable, tape, belt, or material flow

