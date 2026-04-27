// Preview vs production OpenSCAD mode pattern.
// Export only with mode="production".

mode = "preview";
preview = "preview";
production = "production";
cutaway = "cutaway";

is_preview = mode == "preview";
is_production = mode == "production";
is_cutaway = mode == "cutaway";

show_pcb_placeholder = true;
show_clearance_preview = true;

module printable_part() {
    cube([40, 30, 6]);
}

module pcb_placeholder() {
    %color([0.1, 0.4, 1.0, 0.25])
        translate([5, 5, 6])
            cube([30, 20, 1.6]);
}

module clearance_preview() {
    %color([0.2, 1.0, 0.2, 0.20])
        translate([3, 3, 6])
            cube([34, 24, 8]);
}

module production_geometry() {
    printable_part();
}

module preview_helpers() {
    if (is_preview && show_pcb_placeholder)
        pcb_placeholder();

    if (is_preview && show_clearance_preview)
        clearance_preview();
}

module main() {
    production_geometry();
    preview_helpers();
}

main();

