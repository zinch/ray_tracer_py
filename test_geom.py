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

