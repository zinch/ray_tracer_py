from core.geom import Point
from core.matrix import rotation_x, rotation_y, rotation_z, shearing

import math

def test_rotating_point_around_x_axis():
    p = Point(0, 1, 0)
    half_quarter = rotation_x(math.pi / 4)
    full_quarter = rotation_x(math.pi / 2)

    half_quarter_pt = half_quarter * p
    full_quarter_pt = full_quarter * p

    assert half_quarter_pt == Point(0, math.sqrt(2)/2, math.sqrt(2)/2)
    assert full_quarter_pt == Point(0, 0, 1)

def test_rotating_around_x_axis_in_opposite_direction():
    p = Point(0, 1, 0)
    half_quarter = rotation_x(math.pi / 4)
    inverse = half_quarter.inverse()

    half_quarter_pt = inverse * p

    assert half_quarter_pt == Point(0, math.sqrt(2)/2, -math.sqrt(2)/2)

def test_rotating_around_y_axis():
    p = Point(0, 0, 1)
    half_quarter = rotation_y(math.pi / 4)
    full_quarter = rotation_y(math.pi / 2)

    half_quarter_pt = half_quarter * p
    full_quarter_pt = full_quarter * p

    assert half_quarter_pt == Point(math.sqrt(2)/2, 0, math.sqrt(2)/2)
    assert full_quarter_pt == Point(1, 0, 0)

def test_rotating_around_z_axis():
    p = Point(0, 1, 0)
    half_quarter = rotation_z(math.pi / 4)
    full_quarter = rotation_z(math.pi / 2)

    half_quarter_pt = half_quarter * p
    full_quarter_pt = full_quarter * p

    assert half_quarter_pt == Point(-math.sqrt(2)/2, math.sqrt(2)/2, 0)
    assert full_quarter_pt == Point(-1, 0, 0)

def test_shearing_transformation_of_x_in_proportion_to_y():
    transform = shearing(1, 0, 0, 0, 0, 0)
    p = Point(2, 3, 4)

    new_point = transform * p

    assert new_point == Point(5, 3, 4)

def test_shearing_transformation_of_x_in_proportion_to_z():
    transform = shearing(0, 1, 0, 0, 0, 0)
    p = Point(2, 3, 4)

    new_point = transform * p

    assert new_point == Point(6, 3, 4)

def test_shearing_transformation_of_y_in_proportion_to_x():
    transform = shearing(0, 0, 1, 0, 0, 0)
    p = Point(2, 3, 4)

    new_point = transform * p

    assert new_point == Point(2, 5, 4)

def test_shearing_transformation_of_y_in_proportion_to_z():
    transform = shearing(0, 0, 0, 1, 0, 0)
    p = Point(2, 3, 4)

    new_point = transform * p

    assert new_point == Point(2, 7, 4)

def test_shearing_transformation_of_z_in_proportion_to_x():
    transform = shearing(0, 0, 0, 0, 1, 0)
    p = Point(2, 3, 4)

    new_point = transform * p

    assert new_point == Point(2, 3, 6)

def test_shearing_transformation_of_z_in_proportion_to_y():
    transform = shearing(0, 0, 0, 0, 0, 1)
    p = Point(2, 3, 4)

    new_point = transform * p

    assert new_point == Point(2, 3, 7)

