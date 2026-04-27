# Heat-Set Insert PCB Standoff

## Summary

A PCB standoff with a heat-set insert should have enough boss diameter, insert depth, base support, and gussets.

## Why It Matters

PCB screws must hold under vibration without splitting the boss or loading the PCB unevenly.

## Good Pattern

- Insert pilot hole.
- Adequate boss OD.
- Base pad.
- Gussets into the floor.
- Tool access.

## Correct Design Rule

An insert boss is structural. It should not be an isolated cylinder.

## OpenSCAD/CAD Notes

Make `insert_hole_diameter` and `insert_depth` parameters. Do not hide actual insert dimensions.

## Manufacturing Notes

Print a test coupon for actual inserts. Use controlled heat and keep the insert aligned.

## Tags

heat-set-insert, pcb, standoff, boss, fastener

