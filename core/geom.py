import math
from core.tuple import Tuple
from core.math_util import equal

class Base:
    def __init__(self, x, y, z, w):
        self.t = Tuple(x, y, z, w)

    def __str__(self):
        return str(self.t)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Base):
            raise ValueError('Can compare only tuples')

        return self.t == other.t

    def is_point(self):
        return self.t[3] == 1

    def is_vector(self):
        return self.t[3] == 0

    def __add__(self, other):
        if not isinstance(other, Base):
            raise ValueError('Can add only tuples')

        if self.is_point() and other.is_point():
            raise ValueError('Cannot add points')

        x, y, z, w = self.t + other.t
        if w == 0:
            return Vector(x, y, z)
        else:
            return Point(x, y, z)

    def __sub__(self, other):
        if not isinstance(other, Base):
            raise ValueError('Can subtract only tuples')

        if self.is_vector() and other.is_point():
            raise ValueError('Cannot subtract point from a vector')

        x, y, z, w = self.t - other.t
        if w == 0:
            return Vector(x, y, z)
        else:
            return Point(x, y, z)


class Point(Base):
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 1)

class Vector(Base):
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 0)

    def __neg__(self):
        x, y, z, _ = -self.t
        return Vector(x, y, z)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            x, y, z, _ = self.t * other
            return Vector(x, y, z)
        elif isinstance(other, Vector):
            x1, y1, z1, _ = self.t.values
            x2, y2, z2, _ = other.t.values
            return x1 * x2 + y1 * y2 + z1 * z2
        else:
            raise ValueError(f'Cannot multiply by {other}')

    def magnitude(self):
        x, y, z, _ = self.t.values
        return math.sqrt(x ** 2 + y ** 2 + z ** 2)

    def normalize(self):
        m = self.magnitude()
        x, y, z, _ = self.t.values
        return Vector(x / m, y / m, z / m)

    def cross(self, other):
        if isinstance(other, Vector):
            x1, y1, z1, _ = self.t.values
            x2, y2, z2, _ = other.t.values

            x = y1 * z2 - z1 * y2
            y = z1 * x2 - x1 * z2
            z = x1 * y2 - y1 * x2
            return Vector(x, y, z)
        else:
            raise ValueError(f'Cannot multiply by {other}')

