class Tuple():
    def __init__(self, x, y, z, w):
        self.values = (x, y, z, w)

    def is_point(self):
        return self.values[3] == 1

    def is_vector(self):
        return self.values[3] == 0

    def __add__(self, other):
        if self.is_point() and other.is_point():
            raise ValueError("Cannot add points")

        x1, y1, z1, w1 = self.values
        x2, y2, z2, w2 = other.values
        w = w1 + w2
        if w == 0:
            return Vector(x1 + x2, y1 + y2, z1 + z2)
        else:
            return Point(x1 + x2, y1 + y2, z1 + z2)

    def __sub__(self, other):
        if self.is_vector() and other.is_point():
            raise ValueError("Cannot subtract point from a vector")
        x1, y1, z1, w1 = self.values
        x2, y2, z2, w2 = other.values

        w = w1 - w2
        if w == 0:
            return Vector(x1 - x2, y1 - y2, z1 - z2)
        else:
            return Point(x1 - x2, y1 - y2, z1 - z2)


class Point(Tuple):
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 1)


class Vector(Tuple):
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 0)


