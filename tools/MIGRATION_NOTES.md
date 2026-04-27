# Tools Migration Notes

The requested target structure names this folder `Tools`, but the current physical folder is:

```text
C:\Users\LJ\CAD Projects\tools
```

On Windows, this resolves when addressed as:

```text
C:\Users\LJ\CAD Projects\Tools
```

Do not rename it automatically. Existing scripts, the venv, and output paths use lowercase `tools`.

Recommended future handling:

1. Keep using `tools` for existing scripts until each path reference is audited.
2. Document new scripts as `Tools` in high-level architecture docs, while using actual existing paths when invoking commands.
3. If case normalization is desired later, rename only after a path search confirms no hardcoded lowercase references need to remain.

