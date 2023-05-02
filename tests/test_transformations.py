from core.geom import Point, Vector
from core.matrix import translation

def test_translation():
    transform = translation(5, -3, 2)
    p = Point(-3, 4, 5)

    new_point = transform * p

    assert new_point == Point(2, 1, 7)

def test_multiplying_by_inverse_of_translation_matrix():
    transform = translation(5, -3, 2)
    inverse = transform.inverse()
    p = Point(-3, 4, 5)

    new_point = inverse * p

    assert new_point == Point(-8, 7, 3)

def test_translation_not_affecting_vectors():
    transform = translation(5, -3, 2)
    v = Vector(-3, 4, 5)

    assert transform * v == v
