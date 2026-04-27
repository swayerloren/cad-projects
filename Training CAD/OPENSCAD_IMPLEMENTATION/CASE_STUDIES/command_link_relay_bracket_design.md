# Case Study: Command Link Relay Bracket Design

The Command Link lid had relay insert bosses but no actual removable bracket
parts. The fix was to create a separate bracket SCAD file and a shared relay
layout file.

Files created:

- `command_link_relay_layout_dimensions.scad`
- `command_link_relay_brackets.scad`

The bracket file supports:

- preview with relay placeholders and screw alignment
- one-bracket production export
- five-bracket production-set export

Lesson: mount zones are not the same as real retainers. If the product needs
serviceable clamps, export those clamps as their own printable parts.
