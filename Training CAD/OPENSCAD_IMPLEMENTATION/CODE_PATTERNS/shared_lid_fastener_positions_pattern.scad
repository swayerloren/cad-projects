// Pattern: one shared fastener layout for base insert bosses and lid holes.

lid_fastener_edge_offset = 6.0;

function lid_fastener_positions(body_w, body_l, edge_offset = lid_fastener_edge_offset) = [
    [edge_offset, edge_offset],
    [body_w - edge_offset, edge_offset],
    [edge_offset, body_l - edge_offset],
    [body_w - edge_offset, body_l - edge_offset],
    [edge_offset, body_l / 2],
    [body_w - edge_offset, body_l / 2]
];

module base_insert_bosses(body_w, body_l) {
    for (p = lid_fastener_positions(body_w, body_l))
        translate([p[0], p[1], 0])
            difference() {
                cylinder(h = 6, d = 8);
                translate([0, 0, 1])
                    cylinder(h = 5.1, d = 4.2);
            }
}

module lid_screw_clearance_holes(body_w, body_l, lid_h) {
    for (p = lid_fastener_positions(body_w, body_l))
        translate([p[0], p[1], -0.5])
            cylinder(h = lid_h + 1, d = 3.4);
}
