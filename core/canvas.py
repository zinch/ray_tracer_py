from core.color import Color

class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        black = Color(0, 0, 0)
        self.pixels = [black for x in range(0, width * height)]

    def write_pixel(self, x, y, color):
        self.pixels[self.index(x, y)] = color

    def pixel_at(self, x, y):
        return self.pixels[self.index(x, y)]

    def index(self, x, y):
        return y + self.height + x
