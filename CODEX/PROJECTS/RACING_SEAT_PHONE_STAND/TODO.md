# TODO

- Add a more exact sculpted seat shell using lofted section profiles.
- Add optional underside ribs to the base.
- Add alternate cable cutout positions for side charging ports.
- Add rubber pad recesses.
- Add a support-free simplified rollcage variant.
- Add configurable raised/debossed branding text.
- Add phone fit test placeholders for common phone sizes.

## Quality Rules From Refinement Pass

- Do a visual accuracy review for every styled STL rebuild.
- Compare silhouette and proportions, not only X/Y/Z bounding boxes.
- Always add a functional placeholder for phone/tablet/fixture stands.
- For rollcages, trace hoop/leg/brace logic before coding tubes.
- Do not accept a rebuild that looks mechanically and stylistically wrong even if dimensions are close.

## V2 Follow-Up

- Improve organic seat shell curvature with lofted section profiles if a future workflow allows it.
- Add exact base branding/text if needed.
- Add alternate phone placeholder presets for common phone/case sizes.
- Consider splitting roll cage for support-free printing.
- Add more accurate STL-to-rebuild alignment transforms if original assembly coordinates are recovered.
- Use V2 as the preferred training example over the earlier rebuild.

## Photo Review Follow-Up

- Decode and inspect `il_fullxfull.4555133407_r1h8.avif` with AVIF-capable tooling if exact details from that file are needed.
- Refine rail side cutouts to more closely match the side photo.
- Improve roll cage top hoop continuity with a better curved tube approximation if render cost stays reasonable.
- Improve molded/organic seat shell transitions beyond the current OpenSCAD-safe approximation.
- Keep `REFERENCE_PHOTO_REVIEW.md` updated whenever new reference images are added.

## V3 Follow-Up

- Improve the V3 bucket shell with better lofted cross sections if OpenSCAD performance allows it.
- Replace triangular tube web approximations with closer gray side-plate cutouts if exact side-rail geometry is required.
- Tune roll cage points against more precise side/front photo measurements.
- Add optional no-phone render mode screenshots for pure product comparison.
- Decode the AVIF reference image with AVIF-capable tooling.
- Consider a V4 only if V3 still fails visual review after user inspection.
