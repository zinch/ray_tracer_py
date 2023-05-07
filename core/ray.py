from core.geom import Point
from core.objects import Sphere

import math

class Intersections:
    def __init__(self, intersections):
        self.intersections = intersections[:]
        self.count = len(self.intersections)

    def __getitem__(self, key):
        return self.intersections[key]

class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def position(self, t):
        return self.origin + self.direction * t

    def intersect(self, obj):
        if not isinstance(obj, Sphere):
            return Intersections([])

        sphere_to_ray = self.origin - Point(0, 0, 0)
        a = self.direction * self.direction
        b = 2 * (self.direction * sphere_to_ray)
        c = sphere_to_ray * sphere_to_ray - 1

        discriminant = b ** 2 - 4 * a * c

        if discriminant < 0:
            return Intersections([])

        t1 = (-b - math.sqrt(discriminant)) / (2 * a)
        t2 = (-b + math.sqrt(discriminant)) / (2 * a)

        return Intersections([(t1, obj), (t2, obj)])
