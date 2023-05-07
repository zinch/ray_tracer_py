from core.geom import Point, Vector
from core.objects import Sphere
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

def test_intersecting_sphere_at_two_points():
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = Sphere()

    intersections = r.intersect(s)

    assert len(intersections) == 2
    (t1, obj) = intersections[0]
    assert t1 == 4.0
    assert obj == s

    (t2, obj) = intersections[1]
    assert t2 == 6.0
    assert obj == s

def test_intersecting_sphere_at_tangent():
    r = Ray(Point(0, 1, -5), Vector(0, 0, 1))
    s = Sphere()

    intersections = r.intersect(s)

    assert len(intersections) == 2
    assert intersections[0][0] == 5.0
    assert intersections[1][0] == 5.0

def test_missing_a_sphere():
    r = Ray(Point(0, 2, -5), Vector(0, 0, 1))
    s = Sphere()

    intersections = r.intersect(s)

    assert len(intersections) == 0

def test_intersecting_sphere_from_inside():
    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
    s = Sphere()

    intersections = r.intersect(s)

    assert len(intersections) == 2
    assert intersections[0][0] == -1.0
    assert intersections[1][0] == 1.0

def test_intersecting_sphere_behind_ray():
    r = Ray(Point(0, 0, 5), Vector(0, 0, 1))
    s = Sphere()

    intersections = r.intersect(s)

    assert len(intersections) == 2
    assert intersections[0][0] == -6.0
    assert intersections[1][0] == -4.0


