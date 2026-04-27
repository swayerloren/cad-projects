// PCB standoff pattern using PCB-local coordinate mapping.

$fn = 48;

pcb_width = 65;
pcb_length = 78.71;
pcb_origin_x = 10;
pcb_origin_y = 10;
floor_thickness = 4;
standoff_height = 5;
standoff_outer_diameter = 7;
insert_hole_diameter = 4.2;
insert_depth = 5;

mounting_hole_positions = [
    [2.6, 2.9],
    [62.19, 2.9],
    [2.6, 75.5],
    [62.19, 75.5]
];

function pcb_x(x) = pcb_origin_x + x;
function pcb_y(y) = pcb_origin_y + y;

module standoff_at(x, y) {
    translate([pcb_x(x), pcb_y(y), floor_thickness])
        difference() {
            cylinder(h = standoff_height, d = standoff_outer_diameter);
            translate([0, 0, standoff_height - insert_depth - 0.02])
                cylinder(h = insert_depth + 0.04, d = insert_hole_diameter);
        }
}

module screw_access_preview(x, y) {
    %color([1, 1, 0, 0.25])
        translate([pcb_x(x), pcb_y(y), floor_thickness + standoff_height])
            cylinder(h = 25, d = 8);
}

cube([pcb_width + 20, pcb_length + 20, floor_thickness]);
for (p = mounting_hole_positions) {
    standoff_at(p[0], p[1]);
    screw_access_preview(p[0], p[1]);
}

%color([0.1, 0.45, 1, 0.25])
    translate([pcb_origin_x, pcb_origin_y, floor_thickness + standoff_height])
        cube([pcb_width, pcb_length, 1.6]);
