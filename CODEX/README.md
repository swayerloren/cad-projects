# Codex CAD Knowledge Repository

Root:

```text
C:\Users\LJ\CAD Projects\CODEX
```

This folder stores project memory and instructions for CAD work. It is not the CAD source folder.

Actual project source should normally live under:

- `C:\Users\LJ\CAD Projects\OpenSCAD Projects`
- `C:\Users\LJ\CAD Projects\FreeCAD Projects`
- an existing legacy project folder when the user explicitly targets it

Reusable training lessons belong in:

```text
C:\Users\LJ\CAD Projects\Training CAD
```

Each separate project gets its own memory folder under:

```text
C:\Users\LJ\CAD Projects\CODEX\PROJECTS
```

Before editing any CAD project, verify the exact target path and read the relevant project memory.

Use this repository to preserve:

- Known facts and dimensions.
- Project-specific instructions.
- Design decisions.
- Mistakes and corrections.
- OpenSCAD parameters.
- FreeCAD parameters.
- Manufacturing notes.
- Source and export paths.
- Review notes from renders and screenshots.
- Prompts that worked well.

OpenSCAD is preferred for parametric/code-driven mechanical systems. FreeCAD is preferred for STEP/solid CAD, sketches, constraints, fillets/chamfers, assemblies, and surface-heavy work.

Never silently edit similarly named folders. Before a final response, verify exact files modified.

Repo-level memory files:

- `REPO_MEMORY.md` records current repo structure and rules.
- `REPO_HISTORY.md` records root migration and architecture history.
- `ACTIVE_PROJECTS.md` indexes active and discovered projects.
