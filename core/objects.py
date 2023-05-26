from core.geom import Point
from core.matrix import IDENTITY_MATRIX

CENTER = Point(0, 0, 0)

class Sphere:
    def __init__(self):
        self.transform = IDENTITY_MATRIX

    def set_transform(self, transform):
        self.transform = transform

    def normal_at(self, point):
        return (point - CENTER).normalize()

