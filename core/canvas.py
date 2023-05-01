import math

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
        return x + self.width * y

def to_ppm_format(canvas):
    def scale(value):
        value = max(0, value)
        return min(math.ceil(value * 255), 255)

    lines = []
    for j in range(0, canvas.height):
        colors = []
        for i in range(0, canvas.width):
            p = canvas.pixel_at(i, j)
            txt = f'{scale(p.red())} {scale(p.green())} {scale(p.blue())}'
            colors.insert(i, txt)

        lines.insert(j, ' '.join(colors))

    lines = '\n'.join(lines)
    return f'''
P3
{canvas.width} {canvas.height}
255
{lines}
'''

