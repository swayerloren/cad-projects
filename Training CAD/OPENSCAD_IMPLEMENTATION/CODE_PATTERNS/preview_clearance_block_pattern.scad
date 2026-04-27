// Preview clearance block pattern.
// Preview helpers show fit and service paths without becoming production geometry.

$fn = 32;

show_pcb = true;
show_zip_tie_path = true;
show_wire_bundle = true;
show_screw_access = true;

module production_body() {
    cube([80, 60, 4]);
}

module pcb_preview() {
    if (show_pcb)
        %color([0.1, 0.45, 1.0, 0.25])
            translate([10, 10, 8])
                cube([55, 40, 1.6]);
}

module zip_tie_path_preview() {
    if (show_zip_tie_path)
        %color([0.0, 0.8, 1.0, 0.35])
            translate([5, 20, 4.2])
                cube([4, 20, 1.4]);
}

module wire_bundle_preview() {
    if (show_wire_bundle)
        %color([1.0, 0.35, 0.0, 0.3])
            translate([7, 30, 12])
                rotate([90, 0, 0])
                    cylinder(h = 35, d = 5, center = true);
}

module screw_access_preview() {
    if (show_screw_access)
        %color([1.0, 1.0, 0.0, 0.25])
            translate([20, 20, 4])
                cylinder(h = 35, d = 8);
}

production_body();
pcb_preview();
zip_tie_path_preview();
wire_bundle_preview();
screw_access_preview();
