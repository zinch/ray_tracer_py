import math

from core.color import Color

MAX_LINE_LEN = 70

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

    def split_long_line(line):
        split_idx = line.rfind(' ', 0, MAX_LINE_LEN)
        short_line = line[:split_idx]
        rest = line[split_idx + 1:]
        return (short_line, rest)

    lines = []
    for j in range(0, canvas.height):
        colors = []
        for i in range(0, canvas.width):
            p = canvas.pixel_at(i, j)
            txt = f'{scale(p.red())} {scale(p.green())} {scale(p.blue())}'
            colors.insert(i, txt)

        line = ' '.join(colors)
        if len(line) > MAX_LINE_LEN:
            short_line, rest = split_long_line(line)
            lines.append(short_line)
            lines.append(rest)
        else:
            lines.append(line)

    lines = '\n'.join(lines)
    return f'''
P3
{canvas.width} {canvas.height}
255
{lines}
'''

