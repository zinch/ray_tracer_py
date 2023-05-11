from core.canvas import Canvas, to_ppm_format
from core.color import Color
from core.geom import Point, Vector
from core.objects import Sphere
from core.ray import Ray

import math

CANVAS_PIXELS = 100

canvas = Canvas(CANVAS_PIXELS, CANVAS_PIXELS)
color = Color(0.8, 1, 0)

ray_origin = Point(0, 0, -5)
wall_z = 10
wall_size = 7.0
pixel_size = wall_size / CANVAS_PIXELS
half = wall_size / 2

sphere = Sphere()

for y in range(0, CANVAS_PIXELS):
    world_y = half - pixel_size * y

    for x in range(0, CANVAS_PIXELS):
        world_x = -half + pixel_size * x

        position = Point(world_x, world_y, wall_z)
        ray = Ray(ray_origin, (position - ray_origin).normalize())

        intersections = ray.intersect(sphere)
        hit = intersections.find_hit()
        if hit:
            canvas.write_pixel(x, y, color)

with open('output/circle.ppm', 'w') as f:
    f.write(to_ppm_format(canvas))
