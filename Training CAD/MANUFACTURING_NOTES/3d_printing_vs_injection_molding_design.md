# 3D Printing Vs Injection Molding Design

FDM 3D printing and injection molding reward different design choices.

## FDM 3D Printing

Design for:

- layer direction
- nozzle size
- wall count
- support avoidance
- bridge limits
- heat resistance
- screw and insert strength
- accessible support removal

Useful FDM features:

- thicker ribs than injection-molded ribs
- chamfers instead of unsupported horizontal overhangs
- heat-set insert bosses
- print-orientation-aware gussets
- serviceable screw access

## Injection Molding

Design for:

- nominal wall thickness
- draft
- tooling direction
- ejector access
- sink avoidance
- rib thickness relative to wall thickness
- boss support without thick material masses
- parting lines and shutoffs

Injection-molded design should avoid large solid masses and sudden wall-thickness changes.

## Shared Rule

Design load paths first. Manufacturing details should support the load path, not hide a weak design.

