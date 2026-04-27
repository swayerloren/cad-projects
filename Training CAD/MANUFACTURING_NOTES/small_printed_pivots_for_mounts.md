# Small Printed Pivots For Mounts

## Observed Pattern

The crane arm phone mount uses many D2.8-D3.4 holes in thin printed brackets. These are likely small screws, pins, or clearance holes for M3-class hardware.

## Risks

- holes ovalize with repeated movement
- thin arms crack at the hole tangent
- overtightened screws crush plastic
- printed pins wear quickly

## Better Practice

- Add boss diameter at least 2.5x screw diameter where space allows.
- Use washers on moving joints.
- Use heat-set inserts where disassembly matters.
- Add `pivot_clearance` as a parameter instead of hard-coding one hole diameter.
- Ream or drill critical holes after printing when exact fit matters.
