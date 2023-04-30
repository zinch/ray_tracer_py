import pytest

from core.geom import *

def test_point_creation():
    p = Point(4, -4, 3)
    assert p.t == Tuple(4, -4, 3, 1)

def test_vector_creation():
    v = Vector(4, -4, 3)
    assert v.t == Tuple(4, -4, 3, 0)

def test_adding_two_tuples():
    p = Point(3, -2, 5)
    v = Vector(-2, 3, 1)

    result = p + v

    assert result.t == Tuple(1, 1, 6, 1)

def test_adding_two_points():
    p1 = Point(3, -2, 5)
    p2 = Point(-2, 3, 1)

    with pytest.raises(ValueError):
        result = p1 + p2

def test_subtracting_two_points():
    p1 = Point(3, 2, 1)
    p2 = Point(5, 6, 7)

    result = p1 - p2

    assert result.t == Tuple(-2, -4, -6, 0)

def test_subtracting_vector_from_point():
    p = Point(3, 2, 1)
    v = Vector(5, 6, 7)

    result = p - v

    assert result.t == Tuple(-2, -4, -6, 1)

def test_subtracting_two_vectors():
    v1 = Vector(3, 2, 1)
    v2 = Vector(5, 6, 7)

    result = v1 - v2

    assert result.t == Tuple(-2, -4, -6, 0)

def test_subtracting_point_from_a_vector():
    p = Point(3, 2, 1)
    v = Vector(5, 6, 7)

    with pytest.raises(ValueError):
        result = v - p
