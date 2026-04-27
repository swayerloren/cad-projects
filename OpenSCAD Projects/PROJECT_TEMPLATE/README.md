# OpenSCAD Project Template

## Run OpenSCAD

Open `scad\main.scad` in OpenSCAD for interactive preview.

## Preview Mode Vs Production Mode

`mode = "preview"` shows production geometry plus helper geometry.

`mode = "production"` shows only exportable production geometry.

Preview helpers must never be included in production STL.

## Export Command

Example command:

```powershell
openscad -o exports\STL\part.stl -D 'mode=\"production\"' scad\main.scad
```

If `openscad` is not on `PATH`, use the installed executable path for that machine.

## Outputs

- STL exports: `exports\STL`
- PNG renders: `exports\PNG`
- Reports/reviews: `exports\Reports`
- Design reviews: `docs`

Create a matching CODEX project memory folder before active work.

