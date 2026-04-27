// Pattern: shared relay positions and bracket screw centers.

relay_count = 5;
relay_w = 28;
relay_d = 28;
relay_spacing = 6;
relay_screw_spacing = 22;

function relay_single_row_width(n = relay_count) =
    n * relay_w + (n - 1) * relay_spacing;

function resolved_relay_layout(body_w, requested = "single_row") =
    (requested == "single_row" && relay_single_row_width(relay_count) <= body_w)
        ? "single_row"
        : "staggered_3_2";

function relay_positions(body_w, body_l, layout = "auto") =
    let(
        resolved = (layout == "auto") ? resolved_relay_layout(body_w) : layout,
        step_x = min(relay_w + relay_spacing, body_w / 2 - relay_w / 2),
        row_y = (relay_d + relay_spacing) / 2
    )
    (resolved == "single_row")
        ? [
            for (i = [0 : relay_count - 1])
                [
                    body_w / 2 + (i - (relay_count - 1) / 2) * (relay_w + relay_spacing),
                    body_l / 2
                ]
          ]
        : [
            [body_w / 2 - step_x, body_l / 2 - row_y],
            [body_w / 2,          body_l / 2 - row_y],
            [body_w / 2 + step_x, body_l / 2 - row_y],
            [body_w / 2 - step_x / 2, body_l / 2 + row_y],
            [body_w / 2 + step_x / 2, body_l / 2 + row_y]
          ];

function relay_bracket_screw_positions(center) = [
    [center[0], center[1] - relay_screw_spacing / 2],
    [center[0], center[1] + relay_screw_spacing / 2]
];
