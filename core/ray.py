from core.geom import Point
from core.objects import Sphere

import math

class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def position(self, t):
        return self.origin + self.direction * t

    def intersect(self, obj):
        if not isinstance(obj, Sphere):
            return []

        sphere_to_ray = self.origin - Point(0, 0, 0)
        a = self.direction * self.direction
        b = 2 * (self.direction * sphere_to_ray)
        c = sphere_to_ray * sphere_to_ray - 1

        discriminant = b ** 2 - 4 * a * c

        if discriminant < 0:
            return []

        t1 = (-b - math.sqrt(discriminant)) / (2 * a)
        t2 = (-b + math.sqrt(discriminant)) / (2 * a)

        return [(t1, obj), (t2, obj)]
