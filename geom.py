import math
from math_util import equal

class Tuple():
    def __init__(self, x, y, z, w):
        self.values = (x, y, z, w)

    def is_point(self):
        return self.values[3] == 1

    def is_vector(self):
        return self.values[3] == 0

    def __neg__(self):
         raise ValueError('Cannot negate tuple')

    def __mul__(self):
         raise ValueError('Cannot multiply tuple')

    def __add__(self, other):
        if not isinstance(other, Tuple):
            raise ValueError('Can add only tuples')

        if self.is_point() and other.is_point():
            raise ValueError('Cannot add points')

        x1, y1, z1, w1 = self.values
        x2, y2, z2, w2 = other.values
        w = w1 + w2
        if w == 0:
            return Vector(x1 + x2, y1 + y2, z1 + z2)
        else:
            return Point(x1 + x2, y1 + y2, z1 + z2)

    def __sub__(self, other):
        if not isinstance(other, Tuple):
            raise ValueError('Can subtract only tuples')

        if self.is_vector() and other.is_point():
            raise ValueError('Cannot subtract point from a vector')
        x1, y1, z1, w1 = self.values
        x2, y2, z2, w2 = other.values

        w = w1 - w2
        if w == 0:
            return Vector(x1 - x2, y1 - y2, z1 - z2)
        else:
            return Point(x1 - x2, y1 - y2, z1 - z2)

    def __eq__(self, other):
        print('boom')
        if not isinstance(other, Tuple):
            raise ValueError('Can compare only tuples')
        x1, y1, z1, w1 = self.values
        x2, y2, z2, w2 = other.values
        return (equal(x1, x2) and
            equal(y1, y2) and
            equal(z1, z2) and
            equal(w1, w2))


class Point(Tuple):
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 1)


class Vector(Tuple):
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 0)

    def __neg__(self):
        x, y, z, _ = self.values
        return Vector(-x, -y, -z)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            x, y, z, _ = self.values
            return Vector(x * other, y * other, z * other)
        elif isinstance(other, Vector):
            x1, y1, z1, _ = self.values
            x2, y2, z2, _ = other.values
            return x1 * x2 + y1 * y2 + z1 * z2
        else:
            raise ValueError(f'Cannot multiply by {other}')

    def magnitude(self):
        x, y, z, _ = self.values
        return math.sqrt(x ** 2 + y ** 2 + z ** 2)

    def normalize(self):
        m = self.magnitude()
        x, y, z, _ = self.values
        return Vector(x / m, y / m, z / m)

    def cross(self, other):
        if isinstance(other, Vector):
            x1, y1, z1, _ = self.values
            x2, y2, z2, _ = other.values

            x = y1 * z2 - z1 * y2
            y = z1 * x2 - x1 * z2
            z = x1 * y2 - y1 * x2
            return Vector(x, y, z)
        else:
            raise ValueError(f'Cannot multiply by {other}')

