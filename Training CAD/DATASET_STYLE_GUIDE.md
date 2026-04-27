# Dataset Style Guide

Future AI training data should use a consistent structure.

Each training item should include:

- Clear title.
- Problem.
- Bad approach, if relevant.
- Why it failed.
- Corrected approach.
- Key parameters.
- OpenSCAD module, if applicable.
- FreeCAD sketch, body, feature, or macro names, if applicable.
- Manufacturing notes.
- Tags.
- Source project reference.
- Date added.

OpenSCAD implementation records should also include:

- Module names involved.
- Key parameters.
- Coordinate mapping assumptions.
- Boolean operation strategy.
- Cutout/tunnel/slot strategy.
- Preview/debug helpers used.
- Render or serviceability test notes.
- Failure modes avoided.

FreeCAD implementation records should also include:

- Workbench used.
- Sketch constraint strategy.
- Body/part hierarchy.
- Feature order assumptions.
- Fillet/chamfer strategy.
- STEP/STL export settings.
- Macro or Python entry point, if used.

Avoid:

- Secrets.
- Tokens.
- Personal data.
- Irrelevant raw logs.
- Long unedited chat transcripts.
- Source files copied without purpose.

Good training records should teach a reusable design habit, CAD tool-selection habit, or implementation pattern.
