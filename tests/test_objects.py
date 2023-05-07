from core.matrix import IDENTITY_MATRIX, translation
from core.objects import Sphere

def test_sphere_default_transformation():
    s = Sphere()

    assert s.transform == IDENTITY_MATRIX

def test_changing_sphere_transformation():
    s = Sphere()
    t = translation(2, 3, 4)
    s.set_transform(t)

    assert s.transform == t
