// Shared fastener layout pattern for an enclosure base and lid.
// Keep this in a shared dimensions file and include it from both SCAD files.

shared_lid_fastener_edge_offset = 10.0;
shared_lid_screw_clearance_diameter = 3.4;
shared_base_lid_insert_hole_diameter = 4.2;
shared_base_lid_insert_depth = 5.0;
shared_base_lid_insert_boss_od = 8.0;

function lid_fastener_positions(body_w, body_l, edge_offset) = [
    [edge_offset, edge_offset],
    [body_w - edge_offset, edge_offset],
    [edge_offset, body_l - edge_offset],
    [body_w - edge_offset, body_l - edge_offset],
    [edge_offset, body_l / 2],
    [body_w - edge_offset, body_l / 2]
];

module lid_screw_clearance_holes(body_w, body_l, lid_thickness) {
    for (p = lid_fastener_positions(body_w, body_l, shared_lid_fastener_edge_offset))
        translate([p[0], p[1], -0.1])
            cylinder(h = lid_thickness + 0.2, d = shared_lid_screw_clearance_diameter);
}

module base_insert_hole_cuts(body_w, body_l, top_z) {
    for (p = lid_fastener_positions(body_w, body_l, shared_lid_fastener_edge_offset))
        translate([p[0], p[1], top_z - shared_base_lid_insert_depth])
            cylinder(h = shared_base_lid_insert_depth + 0.1, d = shared_base_lid_insert_hole_diameter);
}
