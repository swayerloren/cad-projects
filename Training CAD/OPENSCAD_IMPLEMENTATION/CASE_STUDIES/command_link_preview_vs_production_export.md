# COMMAND LINK Case Study: Preview vs Production Export

## Problem

Preview geometry was mixed into the same top-level OpenSCAD assembly as printable geometry. PCB placeholders, wire zone markers, zip-tie path previews, clearance blocks, and labels could appear in exported STL files.

## Bad Pattern

```scad
module enclosure() {
    production_body();
    pcb_placeholder();
    wire_zone_markers();
    zip_tie_path_preview();
}

enclosure();
```

This makes export mode dependent on manually disabling many toggles.

## Good Pattern

```scad
mode = "preview";
is_preview = mode == "preview";
is_production = mode == "production";

module production_geometry() {
    production_body();
}

module preview_helpers() {
    if (is_preview && show_pcb_placeholder) pcb_placeholder();
    if (is_preview && show_wire_zone_markers) wire_zone_markers();
    if (is_preview && show_zip_tie_path_preview) zip_tie_path_preview();
}

module main() {
    production_geometry();
    preview_helpers();
}
```

## Export Rule

Always export with production mode:

```powershell
openscad -D 'mode="production"' -o part.stl part.scad
```

Production modules must not call helper modules or use helper solids as part of printable unions.

