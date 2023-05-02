import math

from core.geom import Point, Vector
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

    def __call__(self, i, j):
        return self.elements[i * self.dimension + j]

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False

        return (self.dimension == other.dimension and
            all([equal(self.elements[i], other.elements[i])
                for i in range(0, self.dimension * self.dimension)]))

    def __mul__(self, other):
        if not isinstance(other, (Matrix, Point, Vector)) or (
                self.dimension != 4 and self.dimension != other.dimension):
            raise ValueError('Can only multiply 4x4 matrices')

        if isinstance(other, Matrix):
            values = []
            for i in range(0, 4):
                for j in range(0, 4):
                    c = 0
                    for k in range(0, 4):
                        c += self(i, k) * other(k, j)
                    values.append(c)

            return Matrix(tuple(values))

        elif isinstance(other, (Point, Vector)):
            x = sum([self(0, i) * other.t[i] for i in range(0, 4)])
            y = sum([self(1, i) * other.t[i] for i in range(0, 4)])
            z = sum([self(2, i) * other.t[i] for i in range(0, 4)])

            if isinstance(other, Point):
                return Point(x, y, z)
            else:
                return Vector(x, y, z)

    def transpose(self):
        result = []
        for i in range(0, self.dimension):
            for j in range(0, self.dimension):
                result.append(self(j, i))
        return Matrix(tuple(result))

    def submatrix(self, skip_i, skip_j):
        result = []
        for i in range(0, self.dimension):
            for j in range(0, self.dimension):
                if not (i == skip_i or j == skip_j):
                    result.append(self(i, j))
        return Matrix(tuple(result))

    def determinant(self):
        if self.dimension == 2:
            return self.elements[0] * self.elements[3] - self.elements[1] * self.elements[2]

        return sum([self.cofactor(0, i) * self.elements[i] for i in range(0, self.dimension)])

    def minor(self, i, j):
        return self.submatrix(i, j).determinant()

    def cofactor(self, i, j):
        m = self.minor(i, j)
        if i + j % 2 == 0:
            return m
        else:
            return -m

class IdentityMatrix(Matrix):
    def __init__(self):
        super().__init__((
            1, 0, 0, 0,
            0, 1, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1))

    def __mul__(self, other):
        if not isinstance(other, (Matrix, Point, Vector)) or (
                self.dimension != 4 and self.dimension != other.dimension):
            raise ValueError('Can only multiply 4x4 matrices')

        return other

    def transpose(self):
        return self

IDENTITY_MATRIX = IdentityMatrix()

