import pytest

from core.geom import *
from core.math_util import equal

def test_negating_vector():
    assert -Vector(1, -2, 3) == Vector(-1, 2, -3)

def test_multiplying_vector_by_scalar():
    assert Vector(1, -2, 3) * 3.5 == Vector(3.5, -7, 10.5)

def test_multiplying_vector_by_fraction():
    assert Vector(1, -2, 3) * 0.5 == Vector(0.5, -1, 1.5)

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

def test_dot_product():
    a = Vector(1, 2, 3)
    b = Vector(2, 3, 4)

    dot_product = a * b

    assert dot_product == 20

def test_cross_product():
    a = Vector(1, 2, 3)
    b = Vector(2, 3, 4)

    assert a.cross(b) == Vector(-1, 2, -1)
    assert b.cross(a) == Vector(1, -2, 1)

