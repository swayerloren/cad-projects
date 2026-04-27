// Pattern: individual wall-integrated zip-tie clip.
// The slot cuts are applied only to the raised internal clip body.

$fn = 48;

wall_tie_clip_width_y = 14;
wall_tie_clip_height_z = 15;
wall_tie_clip_projection = 3;
wall_tie_slot_width_y = 8;
wall_tie_slot_height_z = 2.7;
wall_tie_center_bridge_height = 4;
wall_tie_slot_corner_radius = 1.2;

module rounded_slot_2d(length, height, radius = 0) {
    r = (radius > 0) ? radius : height / 2;
    hull() {
        translate([-length / 2 + r, 0])
            circle(r = r);
        translate([ length / 2 - r, 0])
            circle(r = r);
    }
}

module rounded_slot_cut(depth, length_y, height_z, zc) {
    translate([-0.05, 0, zc])
        rotate([0, 90, 0])
            linear_extrude(height = depth)
                rounded_slot_2d(length_y, height_z, wall_tie_slot_corner_radius);
}

module clip_pad() {
    translate([wall_tie_clip_projection / 2, 0, wall_tie_clip_height_z / 2])
        cube([
            wall_tie_clip_projection,
            wall_tie_clip_width_y,
            wall_tie_clip_height_z
        ], center = true);
}

module wall_tie_clip() {
    stack_h = 2 * wall_tie_slot_height_z + wall_tie_center_bridge_height;
    z0 = (wall_tie_clip_height_z - stack_h) / 2;
    lower_zc = z0 + wall_tie_slot_height_z / 2;
    upper_zc = z0 + wall_tie_slot_height_z + wall_tie_center_bridge_height + wall_tie_slot_height_z / 2;

    difference() {
        clip_pad();
        rounded_slot_cut(wall_tie_clip_projection + 0.25, wall_tie_slot_width_y, wall_tie_slot_height_z, lower_zc);
        rounded_slot_cut(wall_tie_clip_projection + 0.25, wall_tie_slot_width_y, wall_tie_slot_height_z, upper_zc);
    }
}

wall_tie_clip();
