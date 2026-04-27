# Design Rule: When To Remove Failed Features

Remove a generated feature instead of refining it when:

- several visual passes still miss the target
- the feature starts dictating the whole enclosure layout
- the geometry is less clear than a manual edit would be
- the user explicitly says they will add the feature manually
- keeping the feature risks damaging otherwise accepted geometry

For mechanical CAD, removal is a valid correction. A clean, solid wall is often a better handoff state than a complicated slot system that is not trusted.

## Documentation Pattern

Record:

- what geometry was removed
- what systems were preserved
- what controls keep old code inactive
- what the user will do manually later
- that future agents must not re-add it without explicit instruction
