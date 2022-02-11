#!/home/kincerb/Projects/3d-projects/venv/bin/python
import openpyscad as scad

CHALK_LENGTH = 1
CHALK_HEIGHT = 0.75
PADDING_SIDES = 0.50
PADDING_TOP = 0.50


def create_chalk(width, height, sides=8):
    """
    Create an object representing a piece of chalk

    Args:
        width (float): width of chalk
        height (float): height of chalk
        sides (int): number of sides

    Returns:
        scad.Cylinder: chalk object
    """
    return scad.Cylinder(h=height, d=width, _fn=sides, center=False)


def create_holder_base(chalk_object, padding_top, padding_sides):
    """
    Create and return the base of a chalk holder

    Args:
        chalk_object (scad.Cylinder): chalk object
        padding_top (float): padding on top of chalk
        padding_sides (float): total padding on sides of chalk

    Returns:
        scad.Cylinder: chalk holder base object
    """
    uncut_holder = scad.Cylinder(
        h=(chalk_object.h + padding_top),
        d=(chalk_object.d + padding_sides),
        _fn=100,
        center=False)
    return uncut_holder - chalk_object


def create_holder_top(holder_base):
    """
    Create the top for a chalk holder

    Args:
        holder_base (scad.Cylinder): holder base object

    Returns:
        scad.Sphere: chalk holder top object
    """
    uncut_top = scad.Sphere(d=holder_base.d)
    return uncut_top - scad.Cylinder(h=(holder_base.d / 2), d=holder_base.d)


if __name__ == '__main__':
    chalk = create_chalk(CHALK_LENGTH, CHALK_HEIGHT)
    holder_base = create_holder_base(chalk, PADDING_TOP, PADDING_SIDES)
    holder_base.write('./scad/sample.scad')
