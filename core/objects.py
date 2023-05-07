from core.matrix import IDENTITY_MATRIX

class Sphere:
    def __init__(self):
        self.transform = IDENTITY_MATRIX

    def set_transform(self, transform):
        self.transform = transform
