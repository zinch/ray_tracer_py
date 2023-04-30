from core.math_util import equal

class Tuple:
    def __init__(self, x, y, z, w=0):
        self.values = (x, y, z, w)

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Tuple):
            x1, y1, z1, w1 = self
            x2, y2, z2, w2 = other

            return (equal(x1, x2) and
                    equal(y1, y2) and
                    equal(z1, z2) and
                    equal(w1, w1))

        raise ValueError(f'Cannot compare with {other}')

    def __getitem__(self, key):
        return self.values[key]

    def __add__(self, other):
        if isinstance(other, Tuple):
            x1, y1, z1, w1 = self
            x2, y2, z2, w2 = other

        return Tuple(x1 + x2, y1 + y2, z1 + z2, w1 + w2)

        raise ValueError(f'Cannot add {other}')

    def __sub__(self, other):
        if isinstance(other, Tuple):
            x1, y1, z1, w1 = self
            x2, y2, z2, w2 = other

        return Tuple(x1 - x2, y1 - y2, z1 - z2, w1 - w2)

        raise ValueError(f'Cannot subtract {other}')

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            x, y, z, w = self
            return Tuple(other * x, other * y, other * z, other * w)

        raise ValueError(f'Cannot multiply by {other}')

    def __neg__(self):
        x, y, z, w = self
        return Tuple(-x, -y, -z, -w)
