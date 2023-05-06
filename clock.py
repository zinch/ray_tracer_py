from core.canvas import Canvas, to_ppm_format
from core.color import Color
from core.geom import Point
from core.matrix import IDENTITY_MATRIX

import math

CANVAS_SIZE = 100
canvas = Canvas(CANVAS_SIZE, CANVAS_SIZE)
border_color = Color(0, 0.5, 0.5)

for i in range(0, CANVAS_SIZE, 3):
    canvas.write_pixel(0, i, border_color)
    canvas.write_pixel(CANVAS_SIZE - 1, i, border_color)
    canvas.write_pixel(i, 0, border_color)
    canvas.write_pixel(i, CANVAS_SIZE - 1, border_color)

color = Color(0.75, 0.95, 0.6)

angle = math.pi / 6
point = Point(0, 1, 0)
for i in range(12):
    rotation_angle = angle * i

    transform = (IDENTITY_MATRIX
        .rotate_z(-rotation_angle)
        .scale(CANVAS_SIZE // 2 - 2, CANVAS_SIZE // 2 - 2, 0)
        .translate(CANVAS_SIZE // 2, -CANVAS_SIZE // 2, 0))

    new_point = transform * point
    x = round(new_point.x())
    y = round(new_point.y())

    print(f'i={i}, angle={round(rotation_angle / math.pi * 180)}, x={x}, y={y}')
    canvas.write_pixel(x, y, color)

with open('output/clock.ppm', 'w') as f:
    f.write(to_ppm_format(canvas))
