from core.geom import Point, Vector
from core.ray import Ray

def test_creating_ray():
    origin = Point(1, 2, 3)
    direction = Vector(4, 5, 6)

    r = Ray(origin, direction)

    assert r.origin == origin
    assert r.direction == direction

def test_computing_point_from_distance():
    r = Ray(Point(2, 3, 4), Vector(1, 0, 0))

    p0 = r.position(0)
    assert p0 == Point(2, 3, 4)

    p1 = r.position(1)
    assert p1 == Point(3, 3, 4)

    p_1 = r.position(-1)
    assert p_1 == Point(1, 3, 4)

    p = r.position(2.5)
    assert p == Point(4.5, 3, 4)
