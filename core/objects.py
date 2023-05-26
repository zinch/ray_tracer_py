from core.geom import Point
from core.matrix import IDENTITY_MATRIX

CENTER = Point(0, 0, 0)

class Sphere:
    def __init__(self):
        self.transform = IDENTITY_MATRIX
        self.inverse = IDENTITY_MATRIX
        self.inverse_transpose = IDENTITY_MATRIX

    def set_transform(self, transform):
        self.transform = transform
        self.inverse = transform.inverse()
        self.inverse_transpose = self.inverse.transpose()

    def normal_at(self, point):
        object_point = self.inverse * point
        object_normal = (object_point - CENTER).normalize()
        world_normal = self.inverse_transpose * object_normal
        world_normal.w = 0
        return world_normal.normalize()

