# OpenSCAD Render Testing

## Preview Is Not Enough

F5 preview can show geometry that later fails during CGAL render. F6 render is required before exporting a production STL.

## Basic Test Flow

1. Use F5 preview for fast iteration.
2. Inspect from multiple camera angles.
3. Turn on placeholders and clearance previews.
4. Turn on cutaway/debug views if needed.
5. Run F6 render.
6. Export STL only after render succeeds.

## What To Inspect

- Tunnels and slots from both entrance and exit.
- Interior walls for accidental exterior cuts.
- Screw and insert access.
- PCB placeholder collisions.
- Wire bundle bend path.
- Mount ears and boss holes.
- Non-manifold warnings.

## Feature Coupons

Make small test coupons for:

- Heat-set insert bosses.
- Cable-tie saddle tunnels.
- Grommet/cable gland holes.
- Screw boss and washer bearing surfaces.

Testing a coupon is faster than printing a full enclosure.

## Windows Command-Line Render Example

```powershell
& 'C:\Program Files\OpenSCAD\openscad.exe' -o "$env:TEMP\test.stl" '.\part.scad'
```

Use command-line render tests when automating validation.
