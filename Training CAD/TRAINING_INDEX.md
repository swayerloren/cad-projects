# Training Index

This index covers reusable CAD training material across OpenSCAD, FreeCAD, hybrid CAD workflows, manufacturing, STL reverse engineering, PCB enclosures, brackets, mounts, wire management, heat-set inserts, and future AI/local LLM training data.

| Folder | Purpose |
|---|---|
| `DESIGN_RULES` | General mechanical, OpenSCAD, FreeCAD, and CAD tool-selection standards |
| `OPENSCAD_IMPLEMENTATION` | OpenSCAD coding methods, boolean logic, coordinate mapping, previews, render testing, and code patterns |
| `OPENSCAD_MODULES` | Reusable educational OpenSCAD module examples |
| `FREECAD_IMPLEMENTATION` | FreeCAD project setup, sketch/constraint workflow, macro usage, and STEP/solid CAD workflow notes |
| `FREECAD_MACROS` | Reusable FreeCAD macro examples and training notes |
| `FREECAD_WORKBENCH_NOTES` | Workbench-specific FreeCAD notes |
| `GOOD_EXAMPLES` | Correct design patterns and why they work |
| `BAD_EXAMPLES` | Rejected design patterns and why they fail |
| `BEFORE_AFTER_REVIEWS` | Case studies showing design evolution |
| `ENCLOSURES` | Enclosure-specific rules and lessons |
| `MOUNTS_AND_BRACKETS` | Mounting ear, bracket, gusset, and truss lessons |
| `WIRE_MANAGEMENT` | Cable tie, grommet, cable gland, and strain-relief lessons |
| `HEAT_SET_INSERTS` | Insert boss and threaded insert guidance |
| `PCB_CARRIERS` | PCB mounting, standoffs, clearances, and carrier rules |
| `MANUFACTURING_NOTES` | FDM, injection molding, materials, and vehicle-use notes |
| `STL_REVERSE_ENGINEERING` | Workflows for rebuilding clean parametric CAD from STL/STEP/reference assets |
| `SURFACE_MODELING` | Guidance for surface-heavy, organic, or fillet-heavy CAD that should not be forced into OpenSCAD |
| `PROMPT_TEMPLATES` | Reusable prompt patterns for future Codex work |
| `DATASETS` | JSONL Q/A and design-pattern datasets for retrieval/training |

## CAD Tool Selection

| Topic | Location |
|---|---|
| OpenSCAD vs FreeCAD selection | `DESIGN_RULES/openscad_vs_freecad_selection.md` |
| Hybrid CAD workflow | `DESIGN_RULES/hybrid_cad_workflow.md` |
| FreeCAD project setup | `FREECAD_IMPLEMENTATION/freecad_project_setup.md` |
| FreeCAD macro workflow | `FREECAD_IMPLEMENTATION/freecad_macro_workflow.md` |
| FreeCAD macro project workflow | `FREECAD_IMPLEMENTATION/freecad_macro_project_workflow.md` |
| Racing Seat FreeCAD case study | `FREECAD_IMPLEMENTATION/case_study_racing_seat_phone_stand.md` |
| COMMAND LINK FreeCAD enclosure case study | `FREECAD_IMPLEMENTATION/case_study_command_link_enclosure.md` |
| OpenSCAD project setup | `OPENSCAD_IMPLEMENTATION/openscad_project_setup.md` |
| Preview vs production mode | `OPENSCAD_IMPLEMENTATION/preview_vs_production_mode.md` |
| STL to parametric workflow | `STL_REVERSE_ENGINEERING/stl_to_parametric_workflow.md` |
| STL to parametric or hybrid model | `STL_REVERSE_ENGINEERING/stl_to_parametric_or_hybrid_model.md` |
| When OpenSCAD is not enough | `SURFACE_MODELING/when_openscad_is_not_enough.md` |
| Organic STL reference FreeCAD workflow | `SURFACE_MODELING/organic_stl_reference_freecad_workflow.md` |
| 3D printing vs injection molding | `MANUFACTURING_NOTES/3d_printing_vs_injection_molding_design.md` |
| FreeCAD base/lid fit-check workflow | `ENCLOSURES/freecad_base_lid_fit_check_workflow.md` |

## Recent COMMAND_LINK Lessons

| Lesson | Location |
|---|---|
| Fake cable-tie saddles with no pass-through path | `BAD_EXAMPLES/fake_cable_tie_saddles_no_pass_through.md` |
| Internal cable-tie bridge tunnel | `GOOD_EXAMPLES/internal_cable_tie_bridge_tunnel.md` |
| Hidden or unserviceable zip-tie saddles | `BAD_EXAMPLES/hidden_unserviceable_zip_tie_saddles.md` |
| Serviceable open-top cable-tie saddles | `GOOD_EXAMPLES/serviceable_open_top_cable_tie_saddles.md` |
| Floor-mounted zip-tie tunnels trapped beside PCB | `BAD_EXAMPLES/floor_mounted_zip_tie_tunnels_trapped_beside_pcb.md` |
| Internal wall-integrated zip-tie bridge | `GOOD_EXAMPLES/internal_wall_integrated_zip_tie_bridge.md` |
| Huge wall-to-PCB gap for zip-tie access | `BAD_EXAMPLES/huge_wall_to_pcb_gap_for_zip_tie_access.md` |
| Compact wall-integrated zip-tie service lane | `GOOD_EXAMPLES/compact_wall_integrated_zip_tie_service_lane.md` |
| Preview geometry exported to STL | `BAD_EXAMPLES/preview_geometry_exported_to_stl.md` |
| Production mode clean STL export | `GOOD_EXAMPLES/production_mode_clean_stl_export.md` |
| Wall-integrated zip-tie bridge slots | `WIRE_MANAGEMENT/wall_integrated_zip_tie_bridge_slots.md` |
| COMMAND LINK preview vs production export | `OPENSCAD_IMPLEMENTATION/CASE_STUDIES/command_link_preview_vs_production_export.md` |
| COMMAND LINK wall-integrated zip-tie bridge | `OPENSCAD_IMPLEMENTATION/CASE_STUDIES/command_link_wall_integrated_zip_tie_bridge.md` |
| COMMAND LINK zip-tie mount audit | `OPENSCAD_IMPLEMENTATION/CASE_STUDIES/command_link_zip_tie_mount_audit.md` |
| OpenSCAD manufacturing cleanup for enclosures | `MANUFACTURING_NOTES/openscad_manufacturing_cleanup_for_enclosures.md` |
| Long ladder wall zip-tie rack | `BAD_EXAMPLES/long_ladder_wall_zip_tie_rack.md` |
| Individual wall-integrated zip-tie clip | `GOOD_EXAMPLES/individual_wall_integrated_zip_tie_clip.md` |
| Individual wall zip-tie clip brackets | `WIRE_MANAGEMENT/individual_wall_zip_tie_clip_brackets.md` |
| COMMAND LINK zip-tie reference redesign | `OPENSCAD_IMPLEMENTATION/CASE_STUDIES/command_link_zip_tie_reference_based_redesign.md` |
| Wall-integrated zip-tie clip pattern | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/wall_integrated_zip_tie_clip_pattern.scad` |
| Overcomplicated external mount ears | `BAD_EXAMPLES/overcomplicated_external_mount_ears.md` |
| Simple integrated electronics mounting ear | `GOOD_EXAMPLES/simple_integrated_electronics_mounting_ear.md` |
| Simple integrated mounting ears | `MOUNTS_AND_BRACKETS/simple_integrated_mounting_ears.md` |
| COMMAND LINK external mount redesign | `OPENSCAD_IMPLEMENTATION/CASE_STUDIES/command_link_external_mount_redesign.md` |
| Simple integrated mount ear pattern | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/simple_integrated_mount_ear_pattern.scad` |
| Sealed lid with O-ring groove | `ENCLOSURES/sealed_lid_with_oring_groove.md` |
| Lid relay bracket insert bosses | `HEAT_SET_INSERTS/lid_relay_bracket_insert_bosses.md` |
| Rugged lid relay mounting layout | `GOOD_EXAMPLES/rugged_lid_relay_mounting_layout.md` |
| COMMAND LINK rugged lid design | `OPENSCAD_IMPLEMENTATION/CASE_STUDIES/command_link_rugged_lid_design.md` |
| O-ring groove lid pattern | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/oring_groove_lid_pattern.scad` |
| Relay mount insert boss pattern | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/relay_mount_insert_boss_pattern.scad` |
| Base/lid O-ring seal interface | `ENCLOSURES/base_lid_oring_seal_interface.md` |
| Base insert bosses for service lids | `HEAT_SET_INSERTS/base_insert_bosses_for_service_lids.md` |
| COMMAND LINK base/lid mating fix | `OPENSCAD_IMPLEMENTATION/CASE_STUDIES/command_link_base_lid_mating_fix.md` |
| Matched base/lid fastener layout | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/matched_base_lid_fastener_layout.scad` |
| Lid groove plus base sealing land pattern | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/lid_oring_groove_base_sealing_land.scad` |
| Integrated side-wall service spine | `ENCLOSURES/integrated_side_wall_service_spine.md` |
| Wall-integrated lid bosses with zip-tie spine | `GOOD_EXAMPLES/wall_integrated_lid_bosses_with_zip_tie_spine.md` |
| Separate inboard lid post lane | `BAD_EXAMPLES/separate_inboard_lid_post_lane.md` |
| COMMAND LINK sidewall compaction | `OPENSCAD_IMPLEMENTATION/CASE_STUDIES/command_link_sidewall_compaction.md` |
| Wall-integrated lid insert boss pattern | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/wall_integrated_lid_insert_boss_pattern.scad` |
| COMMAND LINK flush zip-tie wall refactor | `OPENSCAD_IMPLEMENTATION/CASE_STUDIES/command_link_zip_tie_wall_flush_refactor.md` |
| Overworked zip-tie slot design | `BAD_EXAMPLES/overworked_zip_tie_slot_design.md` |
| When to remove failed features | `DESIGN_RULES/when_to_remove_failed_features.md` |
| COMMAND LINK zip-tie slots removed | `OPENSCAD_IMPLEMENTATION/CASE_STUDIES/command_link_zip_tie_slots_removed.md` |
| Waterproof grommet wire entry clearance | `ENCLOSURES/waterproof_grommet_wire_entry_clearance.md` |
| Wire bend radius after grommet | `WIRE_MANAGEMENT/wire_bend_radius_after_grommet.md` |
| COMMAND LINK grommet clearance check | `OPENSCAD_IMPLEMENTATION/CASE_STUDIES/command_link_grommet_clearance_check.md` |
| Grommet hardware clearance preview pattern | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/grommet_hardware_clearance_preview.scad` |
| Grommet hole without inner collar clearance | `BAD_EXAMPLES/grommet_hole_without_inner_collar_clearance.md` |
| Grommet hole with inside/outside clearance | `GOOD_EXAMPLES/grommet_hole_with_inside_outside_clearance.md` |
| COMMAND LINK grommet inner clearance fix | `OPENSCAD_IMPLEMENTATION/CASE_STUDIES/command_link_grommet_inner_clearance_fix.md` |
| Inside grommet collar relief pattern | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/inside_grommet_collar_relief_pattern.scad` |
| Cable gland hole without inner nut clearance | `BAD_EXAMPLES/cable_gland_hole_without_inner_nut_clearance.md` |
| Cable gland with inner/outer landing clearance | `GOOD_EXAMPLES/cable_gland_with_inner_outer_landing_clearance.md` |
| Waterproof cable gland install clearance | `WIRE_MANAGEMENT/waterproof_cable_gland_install_clearance.md` |
| COMMAND LINK cable gland clearance fix | `OPENSCAD_IMPLEMENTATION/CASE_STUDIES/command_link_cable_gland_clearance_fix.md` |
| Cable gland inner nut clearance pattern | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/cable_gland_inner_nut_clearance_pattern.scad` |
| Base/lid fit verification | `ENCLOSURES/base_lid_fit_verification.md` |
| O-ring groove and sealing land alignment | `ENCLOSURES/oring_groove_and_sealing_land_alignment.md` |
| COMMAND LINK base/lid fit check | `OPENSCAD_IMPLEMENTATION/CASE_STUDIES/command_link_base_lid_fit_check.md` |
| Base/lid assembly fit check pattern | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/base_lid_assembly_fit_check_pattern.scad` |
| Shared lid fastener positions pattern | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/shared_lid_fastener_positions_pattern.scad` |
| Serviceable relay retainer brackets | `GOOD_EXAMPLES/serviceable_relay_retainer_brackets.md` |
| Relay bracket to lid insert design | `HEAT_SET_INSERTS/relay_bracket_to_lid_insert_design.md` |
| COMMAND LINK relay bracket design | `OPENSCAD_IMPLEMENTATION/CASE_STUDIES/command_link_relay_bracket_design.md` |
| Removable relay bracket pattern | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/removable_relay_bracket_pattern.scad` |
| Shared relay layout positions pattern | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/shared_relay_layout_positions_pattern.scad` |
| Lid features crossing O-ring channel | `BAD_EXAMPLES/lid_features_crossing_oring_channel.md` |
| Relay clamp with bottom tray | `BAD_EXAMPLES/relay_clamp_with_bottom_tray.md` |
| Open-bottom relay top retainer | `GOOD_EXAMPLES/open_bottom_relay_top_retainer.md` |
| Hard lid seal keepout zone | `ENCLOSURES/hard_lid_seal_keepout_zone.md` |
| COMMAND LINK lid/base/relay fit fix | `OPENSCAD_IMPLEMENTATION/CASE_STUDIES/command_link_lid_base_relay_fit_fix.md` |
| Open-bottom relay clamp pattern | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/open_bottom_relay_clamp_pattern.scad` |

## OpenSCAD Implementation Index

| Topic | Location |
|---|---|
| Module architecture | `OPENSCAD_IMPLEMENTATION/MODULE_ARCHITECTURE.md` |
| Parameter strategy | `OPENSCAD_IMPLEMENTATION/PARAMETER_STRATEGY.md` |
| Coordinate systems | `OPENSCAD_IMPLEMENTATION/COORDINATE_SYSTEMS.md` |
| Boolean operations | `OPENSCAD_IMPLEMENTATION/BOOLEAN_OPERATIONS.md` |
| Tunnels, slots, and cutouts | `OPENSCAD_IMPLEMENTATION/TUNNELS_SLOTS_AND_CUTOUTS.md` |
| Preview and debug helpers | `OPENSCAD_IMPLEMENTATION/PREVIEW_AND_DEBUG_HELPERS.md` |
| Serviceability checks | `OPENSCAD_IMPLEMENTATION/SERVICEABILITY_CHECKS.md` |
| Common OpenSCAD failures | `OPENSCAD_IMPLEMENTATION/COMMON_OPENSCAD_FAILURES.md` |
| Render testing | `OPENSCAD_IMPLEMENTATION/OPENSCAD_RENDER_TESTING.md` |
| Production SCAD template | `OPENSCAD_IMPLEMENTATION/PRODUCTION_SCAD_FILE_TEMPLATE.md` |
| Code patterns | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/` |
| COMMAND LINK implementation case studies | `OPENSCAD_IMPLEMENTATION/CASE_STUDIES/` |
| Preview vs production mode pattern | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/preview_vs_production_mode_pattern.scad` |
| Wall-integrated bridge cut-depth pattern | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/wall_integrated_zip_tie_bridge_pattern.scad` |

## STL Rebuild Quality Lessons

| Lesson | Location |
|---|---|
| Bounding-box-only STL rebuild failure | `BAD_EXAMPLES/bounding_box_only_stl_rebuild.md` |
| Visual-accuracy-checked STL rebuild | `GOOD_EXAMPLES/visual_accuracy_checked_stl_rebuild.md` |
| Before/after visual accuracy review | `BEFORE_AFTER_REVIEWS/stl_rebuild_visual_accuracy_review.md` |
| Visual accuracy tools for STL rebuilds | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/visual_accuracy_tools_for_stl_rebuilds.md` |
| Generic rebuild of styled product | `BAD_EXAMPLES/generic_rebuild_of_styled_product.md` |
| Racing seat phone stand V2 style rebuild | `GOOD_EXAMPLES/racing_seat_phone_stand_v2_style_rebuild.md` |
| Racing seat phone stand V2 case study | `OPENSCAD_IMPLEMENTATION/CASE_STUDIES/racing_seat_phone_stand_v2.md` |
| Tube between points pattern | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/tube_between_points_pattern.scad` |
| Stylized bucket seat pattern | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/stylized_bucket_seat_pattern.scad` |
| Trussed side rail pattern | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/trussed_side_rail_pattern.scad` |
| Photo-guided styled product rebuild | `GOOD_EXAMPLES/photo_guided_styled_product_rebuild.md` |
| Ignoring reference photos in STL rebuild | `BAD_EXAMPLES/ignoring_reference_photos_in_stl_rebuild.md` |
| Racing seat photo-guided rebuild case study | `OPENSCAD_IMPLEMENTATION/CASE_STUDIES/racing_seat_phone_stand_photo_guided_rebuild.md` |
| Photo reference review workflow | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/photo_reference_review_workflow.md` |
| V2 styled product rebuild still wrong | `BAD_EXAMPLES/v2_styled_product_rebuild_still_wrong.md` |
| V3 photo-guided racing seat rebuild | `GOOD_EXAMPLES/v3_photo_guided_racing_seat_rebuild.md` |
| Racing seat phone stand V3 case study | `OPENSCAD_IMPLEMENTATION/CASE_STUDIES/racing_seat_phone_stand_v3.md` |
| Bucket seat shell layered hull pattern | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/bucket_seat_shell_layered_hull_pattern.scad` |
| Roll cage tube frame pattern | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/roll_cage_tube_frame_pattern.scad` |
| Trussed side rail phone stand pattern | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/trussed_side_rail_phone_stand_pattern.scad` |

## Gear Machine Rebuild Lessons

| Lesson | Location |
|---|---|
| Gear-machine rebuild without mechanical accuracy review | `BAD_EXAMPLES/gear_machine_rebuild_without_mechanical_accuracy_review.md` |
| Gear-machine rebuild with pitch debug | `GOOD_EXAMPLES/gear_machine_rebuild_with_pitch_debug.md` |
| Before/after gear mechanical accuracy review | `BEFORE_AFTER_REVIEWS/gear_machine_mechanical_accuracy_review.md` |
| Gear mesh preview and axis debug pattern | `OPENSCAD_IMPLEMENTATION/CODE_PATTERNS/gear_mesh_preview_and_axis_debug.md` |
