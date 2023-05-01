class Matrix:
    def __init__(self, elements):
        if len(elements) != 16:
            raise AssertionError('Only 4x4 matrices are supported')
        self.elements = elements

    def __str__(self):
        xs = [f'{self.elements[i:i + 4]}' for i in [0, 4, 8, 12]]
        return '\n'.join(xs)

    def __repr__(self):
        return self.__str__()

    def __call__(self, x, y):
        idx = x * 4 + y
        print(f'{x},{y} - {idx}')
        return self.elements[idx]
