// Wall-integrated recessed zip-tie bridge pattern.
// The exterior wall remains solid. Slot cuts are limited to the inward pad.

$fn = 40;
eps = 0.02;

wall_thickness = 3.5;
wall_length = 34;
wall_height = 24;

pad_width = 12;
pad_height = 13;
pad_projection = 2.0;
pad_z = 6;
pad_y = wall_length / 2;

slot_width = 7.0;
slot_height = 2.4;
vertical_gap = 3.5;
slot_chamfer = 0.6;
center_bridge_rounding = 0.8;
edge_radius = 1.0;

show_zip_tie_path_preview = true;

function slot_stack_height() = 2 * slot_height + vertical_gap;
function slot_z0() = (pad_height - slot_stack_height()) / 2;
function back_skin() = 0.15;
function front_skin() = min(max(0.55, center_bridge_rounding), pad_projection - 0.35);
function slot_cut_depth() = pad_projection - back_skin();

module rounded_box_2d(w, h, r) {
    rr = max(0.01, min(r, min(w, h) / 2 - 0.01));
    hull()
        for (x = [rr, w - rr])
            for (y = [rr, h - rr])
                translate([x, y])
                    circle(r = rr);
}

module centered_rounded_rect_2d(w, h, r) {
    translate([-w / 2, -h / 2])
        rounded_box_2d(w, h, r);
}

module rounded_yz_cut(depth, width_y, height_z, radius, x0, zc) {
    translate([x0, 0, zc])
        rotate([0, 90, 0])
            linear_extrude(height = depth)
                centered_rounded_rect_2d(height_z, width_y, radius);
}

module wall_segment() {
    color([0.72, 0.72, 0.68])
        cube([wall_thickness, wall_length, wall_height]);
}

module pad_body() {
    translate([0, 0, pad_height / 2])
        rotate([0, 90, 0])
            linear_extrude(height = pad_projection)
                centered_rounded_rect_2d(pad_height, pad_width, edge_radius);
}

module bridge_cutouts() {
    lower_z = slot_z0() + slot_height / 2;
    upper_z = lower_z + slot_height + vertical_gap;
    stack_z = slot_z0() + slot_stack_height() / 2;
    slot_x = pad_projection - slot_cut_depth();
    face_depth = min(slot_chamfer, slot_cut_depth() / 2);

    // Behind-bridge channel stops before the inside face, leaving the center bridge.
    rounded_yz_cut(
        pad_projection - front_skin() - back_skin(),
        slot_width - 0.35,
        slot_stack_height() + 0.25,
        slot_chamfer,
        back_skin(),
        stack_z
    );

    // Lower and upper inside-facing slots.
    rounded_yz_cut(slot_cut_depth() + eps, slot_width, slot_height, slot_chamfer, slot_x, lower_z);
    rounded_yz_cut(slot_cut_depth() + eps, slot_width, slot_height, slot_chamfer, slot_x, upper_z);

    // Shallow larger mouth cuts soften the exposed edges.
    rounded_yz_cut(face_depth + eps, slot_width + 2 * slot_chamfer, slot_height + 2 * slot_chamfer, slot_chamfer, pad_projection - face_depth, lower_z);
    rounded_yz_cut(face_depth + eps, slot_width + 2 * slot_chamfer, slot_height + 2 * slot_chamfer, slot_chamfer, pad_projection - face_depth, upper_z);
}

module wall_integrated_zip_tie_bridge() {
    wall_segment();

    translate([wall_thickness, pad_y, pad_z])
        difference() {
            pad_body();
            bridge_cutouts();
        }
}

module zip_tie_path_preview() {
    if (show_zip_tie_path_preview) {
        lower_z = pad_z + slot_z0() + (slot_height - 1.4) / 2;
        upper_z = lower_z + slot_height + vertical_gap;

        %color([0.05, 0.35, 1.0, 0.35]) {
            translate([wall_thickness + pad_projection / 2, pad_y, lower_z])
                cube([pad_projection + 0.5, 4.0, 1.4], center = true);
            translate([wall_thickness + pad_projection / 2, pad_y, upper_z])
                cube([pad_projection + 0.5, 4.0, 1.4], center = true);
        }
    }
}

wall_integrated_zip_tie_bridge();
zip_tie_path_preview();

