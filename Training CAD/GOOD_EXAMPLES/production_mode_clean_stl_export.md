# Good Example: Production Mode Clean STL Export

## Pattern

A clean OpenSCAD production export uses an explicit mode:

```scad
mode = "preview";
is_preview = mode == "preview";
is_production = mode == "production";

module production_geometry() {
    printable_body();
}

module preview_helpers() {
    if (is_preview && show_pcb_placeholder) pcb_placeholder();
}

production_geometry();
preview_helpers();
```

## Export Command

```powershell
openscad -D 'mode="production"' -o clean_part.stl part.scad
```

## Acceptance Check

The production STL should contain only real printable solids. It should not contain colored preview solids, translucent clearance blocks, labels, placeholders, or material path previews.

