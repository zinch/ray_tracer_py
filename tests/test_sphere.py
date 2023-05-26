from core.geom import Point, Vector
from core.matrix import scaling, rotation_z, translation
from core.objects import Sphere

import math
import pytest

@pytest.fixture
def sphere():
    return Sphere()

def test_normal_on_sphere_at_point_on_x_axis(sphere):
    n = sphere.normal_at(Point(1, 0, 0))

    assert n == Vector(1, 0, 0)

def test_normal_on_sphere_at_point_on_y_axis(sphere):
    n = sphere.normal_at(Point(0, 1, 0))

    assert n == Vector(0, 1, 0)

def test_normal_on_sphere_at_point_on_z_axis(sphere):
    n = sphere.normal_at(Point(0, 0, 1))

    assert n == Vector(0, 0, 1)

def test_normal_on_sphere_at_nonaxial_point(sphere):
    n = sphere.normal_at(Point(math.sqrt(3) / 3, math.sqrt(3) / 3, math.sqrt(3) / 3))

    assert n == Vector(math.sqrt(3) / 3, math.sqrt(3) / 3, math.sqrt(3) / 3)

def test_normal_is_normalized(sphere):
    n = sphere.normal_at(Point(math.sqrt(3) / 3, math.sqrt(3) / 3, math.sqrt(3) / 3))

    assert n == n.normalize()

def test_computing_normal_on_translated_sphere(sphere):
    sphere.set_transform(translation(0, 1, 0))

    n = sphere.normal_at(Point(0, 1.70711, -0.70711))

    assert n == Vector(0, 0.70711, -0.70711)

def test_computing_normal_on_tranformed_sphere(sphere):
    m = scaling(1, 0.5, 1) * rotation_z(math.pi / 5)
    sphere.set_transform(m)

    n = sphere.normal_at(Point(0, math.sqrt(2) / 2, -math.sqrt(2) / 2))

    assert n == Vector(0, 0.97014, -0.24254)
