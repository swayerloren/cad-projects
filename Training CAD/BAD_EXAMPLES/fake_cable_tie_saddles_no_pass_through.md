# Fake Cable-Tie Saddles With No Pass-Through

## Summary

A cable-tie saddle is bad if it only looks like a saddle but does not provide a real physical path for the tie.

## Why It Matters

If the tie cannot enter one side, pass under a bridge, exit the other side, and loop over the wire bundle, the feature will not work in the real part. In vehicle electronics, unusable strain relief leaves solder joints carrying vibration and wire pull loads.

## Bad Pattern

- A shallow indentation that looks like a slot.
- A covered block with no open tunnel.
- A rail shape where the tie path is hidden or impossible.
- A feature placed too close to the PCB, wall, standoff, or solder pads.
- A zip-tie feature that relies on through-wall holes and creates leak paths.

## Correct Design Rule

Every cable-tie feature must have a visible and dimensioned pass-through tunnel. The exterior wall should remain solid unless the opening is an intentional grommet or cable-gland feature.

## OpenSCAD/CAD Notes

Model the tunnel as an explicit clearance volume, and preview it with a translucent block. Check the tunnel width, tunnel height, entry, exit, and wire loop path.

## Manufacturing Notes

FDM prints can shrink or roughen small tunnels. Add clearance beyond the nominal zip-tie size, avoid tiny roof thicknesses, and print a coupon before committing to production.

## Tags

bad-example, cable-tie, zip-tie, strain-relief, enclosure, serviceability
