# COMMAND LINK Zip-Tie Saddle Failures

## What Failed

Several wire strain-relief versions failed before the current serviceable saddle direction:

1. Standalone posts were weak and not integrated.
2. Through-wall slots created exterior leak paths.
3. Blocky saddles looked molded but did not provide a clear pass-through.
4. Side-channel bridge tunnels had real cuts but were too close to the PCB and not serviceable after board installation.

## Why The First Designs Were Not Physically Usable

The code created geometry that looked like a strain-relief feature, but the assembly sequence was not tested:

1. Install PCB.
2. Solder wires.
3. Feed zip ties.
4. Tighten around wire bundle.

If the zip-tie path is under the PCB edge, behind the board, or too close to the wall, the feature fails even if it has a visible tunnel.

## OpenSCAD Causes

- Tunnel cuts were not always visually validated with preview paths.
- Tie features were placed by simple offsets instead of service clearances.
- The PCB placeholder was not treated as an installed obstruction.
- Exterior wall sealing constraints were not encoded as a rule in the feature placement.

## Correct Module Logic

Use modules with clear responsibilities:

```scad
module cable_tie_saddle_tunnel_cut() { ... }
module serviceable_cable_tie_saddle(x, y) { ... }
module zip_tie_path_preview(x, y) { ... }
module wire_bundle_preview(x, y) { ... }
module service_clearance_preview(side, x, y) { ... }
module cable_tie_saddle_layout() { ... }
```

## Correct Placement Logic

- Use six saddles per long side.
- Put saddles in the open channel between PCB and inside wall.
- Parameterize clearance from PCB edge.
- Parameterize clearance from inside wall.
- Use preview blocks to prove both clearances.

## Final Rule

Serviceable zip-tie features must be accessible after PCB installation and soldering. A real tunnel is necessary but not sufficient; the tunnel must be reachable.
