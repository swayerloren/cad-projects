# Design Decisions

- Rebuilt parts as parametric primitives, not mesh conversions.
- Preserved source part centers for assembly preview because the STLs were already positioned together.
- Centered individual part previews for STL overlay comparison.
- Exposed phone size and pivot/screw parameters at the top.
- Used hulls, rounded plates, and cylinders to approximate sculpted arms and brackets.
- Simplified serrations, pockets, and exact organic curves to keep the rebuild editable.
- Used numeric `preview_id` for reliable Windows OpenSCAD command-line rendering.
