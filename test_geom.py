import pytest

from geom import *

def test_point_creation():
    p = point(4, -4, 3)
    assert p == (4, -4, 3, 1)

def test_vector_creation():
    v = vector(4, -4, 3)
    assert v == (4, -4, 3, 0)

def test_adding_two_tuples():
    p = point(3, -2, 5)
    v = vector(-2, 3, 1)

    result = add(p, v)

    assert result == (1, 1, 6, 1)

def test_adding_two_points():
    p1 = point(3, -2, 5)
    p2 = point(-2, 3, 1)

    with pytest.raises(ValueError):
        result = add(p1, p2)

def test_subtracting_two_points():
    p1 = point(3, 2, 1)
    p2 = point(5, 6, 7)

    result = sub(p1, p2)

    assert result == (-2, -4, -6, 0)

def test_subtracting_vector_from_point():
    p = point(3, 2, 1)
    v = vector(5, 6, 7)

    result = sub(p, v)

    assert result == (-2, -4, -6, 1)

