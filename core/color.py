from core.geom import Tuple
from core.math_util import equal

class Color():
    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b

    def __str__(self):
        return f'RGB({self.red}, {self.green}, {self.blue})'

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if not isinstance(other, Color):
            raise ValueError('Can add only colors')

        return Color(self.red + other.red, self.green + other.green, self.blue + other.blue)

    def __sub__(self, other):
        if not isinstance(other, Color):
            raise ValueError('Can subtract only colors')

        return Color(self.red - other.red, self.green - other.green, self.blue - other.blue)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Color(self.red * other, self.green * other, self.blue * other)
        elif isinstance(other, Color):
            r = self.red * other.red
            g = self.green * other.green
            b = self.blue * other.blue
            return Color(r, g, b)

        raise ValueError(f'Can not multiply by {other}')

    def __eq__(self, other):
        if isinstance(other, Color):
            return (equal(self.red, other.red) and
                    equal(self.green, other.green) and
                    equal(self.blue, other.blue))
        return False

