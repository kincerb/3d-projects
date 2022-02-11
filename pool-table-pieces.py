#!/home/kincerb/Projects/3d-projects/venv/bin/python
import openpyscad as scad

PIECE_LENGTH = 4.5
PIECE_HEIGHT = 0.75
PIECE_DEPTH = 0.25


def create_cube(length, depth, height, definition=100):
    """
    Create a random cube

    Arguments:
        length (float): length of cube
        depth (float): depth of cube
        height (float): height of cube

    Keyword Arguments:
        definition (int): Resolution of image
                          Default is 100

    Returns:
        scad.Cube: cube object
    """
    _length_mm = length * 25.4
    _depth_mm = depth * 25.4
    _height_mm = height * 25.4
    return scad.Cube([_length_mm, _depth_mm, _height_mm], _fn=100).color('Blue').rotate([90, 0, 0])


if __name__ == '__main__':
    cube_piece = create_cube(PIECE_LENGTH, PIECE_DEPTH, PIECE_HEIGHT)
    cube_piece.write('./scad/pool-table-cube.scad')
