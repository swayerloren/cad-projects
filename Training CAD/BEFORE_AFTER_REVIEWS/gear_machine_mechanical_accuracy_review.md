# Before/After Review: Gear Machine Mechanical Accuracy

## Before

The STL rebuild had recognizable parts but failed mechanism review:
- simplified tooth blocks
- arbitrary gear centers
- connecting gears not sharing driven gear axes
- no pitch-circle visualization
- no material/cable path preview
- assembly looked randomly stacked

## After

The corrected rebuild:
- uses source shaft holes as shared gear axes
- separates lower and upper gear planes
- places drive gear by pitch-distance intersection
- improves gear teeth with root/pitch/tip points
- adds pitch circles and axis debug lines
- shows the cable/tape path
- records remaining assumptions in a mechanical accuracy review

## Lesson

For mechanical assemblies, visual similarity must include function. A gear machine is not close enough until tooth count, pitch spacing, shared axes, stack order, and material path are reviewed.

