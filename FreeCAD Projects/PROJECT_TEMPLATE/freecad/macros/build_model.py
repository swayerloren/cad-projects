"""FreeCAD project build macro template."""

import FreeCAD as App


def build_model():
    doc = App.newDocument("ProjectTemplate")
    # Add project geometry here.
    doc.recompute()
    return doc


if __name__ == "__main__":
    build_model()

