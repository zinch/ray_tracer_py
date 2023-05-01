import math

from core.math_util import equal

class Matrix:
    def __init__(self, elements):
        size = len(elements)
        self.elements = elements
        self.dimension = math.ceil(math.sqrt(size))
        if size != 16 and size != 9 and size != 4:
            raise AssertionError('Only 4x4, 3x3 and 2x2 matrices are supported')

    def __str__(self):
        xs = [x for x in range(0, self.dimension * self.dimension, self.dimension)]
        return '\n'.join([f'{self.elements[x:x + self.dimension]}' for x in xs])

    def __repr__(self):
        return self.__str__()

    def __call__(self, x, y):
        return self.elements[x * self.dimension + y]

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False

        return (self.dimension == other.dimension and
            all([equal(self.elements[i], other.elements[i])
                for i in range(0, self.dimension * self.dimension)]))

    def __mul__(self, other):
        if not isinstance(other, Matrix) or (
                self.dimension != 4 and self.dimension != other.dimension):
            raise ValueError('Can only multiply 4x4 matrices')

        values = []
        for i in range(0, 4):
            for j in range(0, 4):
                c = 0
                for k in range(0, 4):
                    c += self(i, k) * other(k, j)
                values.append(c)

        return Matrix(tuple(values))

