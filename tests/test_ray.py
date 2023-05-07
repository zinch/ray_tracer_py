from core.geom import Point, Vector
from core.objects import Sphere
from core.ray import Intersections, Ray

import pytest

@pytest.fixture
def s():
    return Sphere()

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

def test_intersecting_sphere_at_two_points(s):
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))

    intersections = r.intersect(s)

    assert intersections.count == 2
    (t1, obj) = intersections[0]
    assert t1 == 4.0
    assert obj == s

    (t2, obj) = intersections[1]
    assert t2 == 6.0
    assert obj == s

def test_intersecting_sphere_at_tangent(s):
    r = Ray(Point(0, 1, -5), Vector(0, 0, 1))

    intersections = r.intersect(s)

    assert intersections.count == 2
    assert intersections[0][0] == 5.0
    assert intersections[1][0] == 5.0

def test_missing_a_sphere(s):
    r = Ray(Point(0, 2, -5), Vector(0, 0, 1))

    intersections = r.intersect(s)

    assert intersections.count == 0

def test_intersecting_sphere_from_inside(s):
    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))

    intersections = r.intersect(s)

    assert intersections.count == 2
    assert intersections[0][0] == -1.0
    assert intersections[1][0] == 1.0

def test_intersecting_sphere_behind_ray(s):
    r = Ray(Point(0, 0, 5), Vector(0, 0, 1))

    intersections = r.intersect(s)

    assert intersections.count == 2
    assert intersections[0][0] == -6.0
    assert intersections[1][0] == -4.0

def test_creating_intersections(s):
    intersections = Intersections([(1, s), (2, s)])

    assert intersections.count == 2
    assert intersections[0] == (1, s)
    assert intersections[1] == (2, s)

def test_hit_when_all_intersections_are_positive(s):
    intersections = Intersections([(1, s), (2, s)])

    hit = intersections.find_hit()

    assert hit == (1, s)

def test_hit_when_some_intersections_are_negative(s):
    intersections = Intersections([(-1, s), (1, s)])

    hit = intersections.find_hit()

    assert hit == (1, s)

def test_hit_when_all_intersections_are_negative(s):
    intersections = Intersections([(-2, s), (-1, s)])

    hit = intersections.find_hit()

    assert hit == None

def test_hit_is_lowest_positive_intersection():
    intersections = Intersections([(5, s), (7, s), (-3, s), (2, s)])

    hit = intersections.find_hit()

    assert hit == (2, s)

