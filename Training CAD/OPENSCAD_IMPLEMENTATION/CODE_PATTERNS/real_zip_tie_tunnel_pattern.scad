// Real zip-tie tunnel pattern.
// Demonstrates a bridge body, an actual tunnel cut, and a preview tie path.

$fn = 32;

bridge_length = 14;
bridge_width = 10;
bridge_height = 7;
tunnel_width = 5.5;
tunnel_height = 3.0;
tie_preview_thickness = 1.4;
show_tie_preview = true;

module bridge_body() {
    cube([bridge_length, bridge_width, bridge_height], center = true);
}

module tunnel_cut() {
    // Overlap beyond the body so the tunnel is a true pass-through.
    translate([0, 0, -bridge_height / 2 + tunnel_height / 2 + 0.2])
        cube([bridge_length + 1.0, tunnel_width, tunnel_height], center = true);
}

module zip_tie_path_preview() {
    if (show_tie_preview)
        %color([0.0, 0.8, 1.0, 0.35])
            translate([0, 0, -bridge_height / 2 + tunnel_height / 2 + 0.2])
                cube([bridge_length + 2.0, 4.0, tie_preview_thickness], center = true);
}

module real_zip_tie_tunnel() {
    difference() {
        bridge_body();
        tunnel_cut();
    }
    zip_tie_path_preview();
}

real_zip_tie_tunnel();
