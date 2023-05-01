import math

class Matrix:
    def __init__(self, elements):
        size = len(elements)
        if size != 16 and size != 9 and size != 4:
            raise AssertionError('Only 4x4, 3x3 and 2x2 matrices are supported')
        self.elements = elements
        self.dimension = math.ceil(math.sqrt(size))

    def __str__(self):
        xs = [x for x in range(0, self.dimension * self.dimension, self.dimension)]
        return '\n'.join([f'{self.elements[x:x + self.dimension]}' for x in xs])

    def __repr__(self):
        return self.__str__()

    def __call__(self, x, y):
        return self.elements[x * self.dimension + y]
