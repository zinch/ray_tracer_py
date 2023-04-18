import pytest

from math_util import equal

def test_unequal_floating_point_numbers():
    x = 1.00001
    y = 1.00000

    assert not equal(x, y)

def test_equal_floating_point_numbers():
    x = 1.000009
    y = 1.00000

    assert equal(x, y)
