import pytest

from geom import *
from math_util import equal

def test_point_creation():
    p = Point(4, -4, 3)
    assert p.values == (4, -4, 3, 1)

def test_vector_creation():
    v = Vector(4, -4, 3)
    assert v.values == (4, -4, 3, 0)

def test_adding_two_tuples():
    p = Point(3, -2, 5)
    v = Vector(-2, 3, 1)

    result = p + v

    assert result.values == (1, 1, 6, 1)
    assert result.is_point()

def test_adding_two_points():
    p1 = Point(3, -2, 5)
    p2 = Point(-2, 3, 1)

    with pytest.raises(ValueError):
        result = p1 + p2

def test_subtracting_two_points():
    p1 = Point(3, 2, 1)
    p2 = Point(5, 6, 7)

    result = p1 - p2

    assert result.values == (-2, -4, -6, 0)

def test_subtracting_vector_from_point():
    p = Point(3, 2, 1)
    v = Vector(5, 6, 7)

    result = p - v

    assert result.values == (-2, -4, -6, 1)

def test_subtracting_two_vectors():
    v1 = Vector(3, 2, 1)
    v2 = Vector(5, 6, 7)

    result = v1 - v2

    assert result.values == (-2, -4, -6, 0)

def test_subtracting_point_from_a_vector():
    p = Point(3, 2, 1)
    v = Vector(5, 6, 7)

    with pytest.raises(ValueError):
        result = v - p

def test_negating_vector():
    v = Vector(1, -2, 3)

    result = -v

    assert result.values == (-1, 2, -3, 0)

def test_multiplying_vector_by_scalar():
    v = Vector(1, -2, 3)

    result = v * 3.5

    assert result.values == (3.5, -7, 10.5, 0)

def test_multiplying_vector_by_fraction():
    v = Vector(1, -2, 3)

    result = v * 0.5

    assert result.values == (0.5, -1, 1.5, 0)

@pytest.mark.parametrize('vector, expected_magnitude',
        [
            (Vector(1, 0, 0), 1),
            (Vector(0, 1, 0), 1),
            (Vector(0, 0, 1), 1),
            (Vector(1, 2, 3), 3.74165),
            (Vector(-1, -2, -3), 3.74165)
        ])
def test_magnitude(vector, expected_magnitude):
    assert equal(vector.magnitude(), expected_magnitude)

@pytest.mark.parametrize('vector, normalized_vector',
        [
            (Vector(4, 0, 0), Vector(1, 0, 0)),
            (Vector(1, 2, 3), Vector(0.26726, 0.53452, 0.80178))
        ])
def test_magnitude(vector, normalized_vector):
    assert vector.normalize() == normalized_vector
    assert vector.normalize().magnitude() == 1
