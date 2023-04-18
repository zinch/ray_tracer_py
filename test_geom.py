import pytest

from geom import point, vector

def test_point_creation():
    p = point(4, -4, 3)
    assert p == (4, -4, 3, 1)

def test_vector_creation():
    v = vector(4, -4, 3)
    assert v == (4, -4, 3, 0)

