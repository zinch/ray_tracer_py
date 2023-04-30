from core.tuple import Tuple

class Color:
    def __init__(self, r, g, b):
        self.t = Tuple(r, g, b)

    def red(self):
        return self.t[0]

    def green(self):
        return self.t[1]

    def blue(self):
        return self.t[2]

    def __str__(self):
        return f'RGB({self.red()}, {self.green()}, {self.blue()})'

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if not isinstance(other, Color):
            raise ValueError('Can add only colors')

        r, g, b, _ = self.t + other.t
        return Color(r, g, b)

    def __sub__(self, other):
        if not isinstance(other, Color):
            raise ValueError('Can subtract only colors')

        r, g, b, _ = self.t - other.t
        return Color(r, g, b)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            r, g, b, _ = self.t * other
            return Color(r, g, b)
        elif isinstance(other, Color):
            r = self.red() * other.red()
            g = self.green() * other.green()
            b = self.blue() * other.blue()
            return Color(r, g, b)

        raise ValueError(f'Can not multiply by {other}')

    def __eq__(self, other):
        if isinstance(other, Color):
            return self.t == other.t
        return False

