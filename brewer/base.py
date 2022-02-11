#!/usr/bin/env python3.9
import openpyscad as scad

DEFINITION = 100
URN_LENGTH = 7.5
URN_DEPTH = 5


def main():
    solid_base = create_solid_base(0.5, 0.5, 0.5)
    recessed_base = cut_out_base(solid_base)
    recessed_base = recessed_base.color('Blue')
    recessed_base.write('../scad/brewer-base.scad')


def create_solid_base(padding_length: float, padding_depth: float, height: float) -> scad.Cube:
    """Create a solid base, slightly larger than object."""
    _length = (URN_LENGTH + padding_length) * 25.4
    _depth = (URN_DEPTH + padding_depth) * 25.4
    _height = height * 25.4
    return scad.Cube([_length, _depth, _height], _fn=DEFINITION)


def cut_out_base(solid_base: scad.Cube, height_percentage: float = 0.50) -> scad.Cube:
    """Remove run footprint from base."""
    base_length, base_depth, base_height = solid_base.size

    cutout_length = URN_LENGTH * 25.4
    cutout_depth = URN_DEPTH * 25.4
    cutout_height = base_height * height_percentage

    cut_out = scad.Cube([cutout_length, cutout_depth, cutout_height], _fn=DEFINITION)

    start_x = (base_length - cutout_length) / 2
    start_y = (base_depth - cutout_depth) / 2

    return solid_base - cut_out.translate([start_x, start_y, cutout_height])


if __name__ == '__main__':
    main()
