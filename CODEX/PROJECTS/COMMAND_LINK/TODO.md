# TODO

1. Verify latest SCAD render.
2. Fix/confirm reinforced mount pods.
3. Confirm circular grommet hole location and diameter.
4. Do not re-add zip-tie slot geometry unless explicitly requested; user will add slots manually later.
5. Confirm PCB fit and screw access.
6. Print small test section if needed.
7. Adjust insert hole diameter for actual heat-set inserts.
8. Adjust grommet hole diameter for actual rubber grommet/cable gland.
9. Update knowledge files after each major design change.
10. Print-check lower-base lid insert bosses added in `command_link_rugged_enclosure.scad`.
11. Print-check base-side sealing land against the lid O-ring groove.
12. Select and test actual O-ring size/durometer/compression.
13. Select actual automotive relay/bracket dimensions and update relay placeholders.
14. Validate lid-mounted relay harness slack or connector strategy so lid removal does not strain PCB wiring.
15. Print test coupons for relay bracket insert bosses and lid O-ring groove.
16. Decide whether lid screws need sealing washers/thread sealant or a revised isolated screw-boss strategy.
17. Physical-check the compact side-wall service spine with the real PCB, wires, lid screws, and inserts.
18. After the user adds manual zip-tie slots, verify they do not conflict with lid insert bosses, sealing land, PCB, or grommet routing.
19. Select and physically test a real 16 mm-panel-hole waterproof rubber grommet or cable gland.
20. Verify the selected grommet/gland inner flange clears the 20 mm wall height, top rim, floor, and lid interface.
21. Verify an 8 mm wire bundle can enter through the grommet and bend inside without colliding with the PCB/components.
## Base/Lid Fit Follow-Up

- Physically test the lid seating depth and 0.35 mm lip clearance on printed parts.
- Select the final 2.0 mm nominal O-ring and test groove compression, water resistance, and screw clamp load.
- Decide whether lid screws inside the seal line need sealing washers, thread sealant, or isolated screw towers.
- Confirm the lid underside relay insert bosses clear the exact populated PCB and harness.
- Tune M3 base insert pilot diameter/depth to the selected heat-set insert.

## Relay Bracket Follow-Up

- Measure the actual automotive relay or relay socket before finalizing the bracket.
- Adjust relay placeholder width/depth/height and capture lip geometry to the measured part.
- Confirm bracket screw access with the lid installed/removed.
- Test printed bracket material for heat and off-road vibration.
- Decide whether a metal retainer strap is needed for production.

## Grommet Inner Relief Follow-Up

- Test-fit the selected 16.0 mm hole waterproof grommet or gland in the printed enclosure.
- Confirm the inside collar seats in the 28.0 mm relief without rocking on the remaining floor/rim geometry.
- Confirm the local relief does not weaken the front wall under cable pull.
- Confirm the wire bundle bend path clears the collar and PCB after the actual cable diameter is known.

## Lid / Relay Fit Follow-Up - 2026-04-27

- Measure actual relay/socket width, depth, height, shoulders, and terminal
  clearance before finalizing the compact 3+2 lid layout.
- Physically test lid seating with the O-ring installed; CAD fit is not enough
  to validate compression force or water sealing.
- Verify the open-bottom relay clamp captures the selected relay/socket without
  blocking terminals or wires.
- Recheck populated PCB clearance under the lid relay bosses and brackets.
- If the measured relay is larger than the placeholder, revise the lid relay
  packaging instead of violating the seal keepout.

## Cable Gland Install Follow-Up - 2026-04-27

- Select the exact waterproof cable gland or rubber grommet.
- Verify the inside retaining nut across-flats / OD is no larger than the
  modeled 34.0 mm tool clearance envelope.
- Test whether fingers or the intended wrench can tighten the retaining nut in
  the printed enclosure.
- Confirm the local rail/ledge relief leaves enough front-wall strength for
  cable pull and vibration.
- Confirm the wire bend path clears the actual gland body and cable diameter.
