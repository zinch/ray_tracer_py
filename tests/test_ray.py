from core.geom import Point, Vector
from core.ray import Ray

def test_creating_ray():
    origin = Point(1, 2, 3)
    direction = Vector(4, 5, 6)

    r = Ray(origin, direction)

    assert r.origin == origin
    assert r.direction == direction
