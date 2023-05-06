from core.canvas import Canvas, to_ppm_format
from core.color import Color
from core.geom import Point, Vector

class Projectile:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def x(self):
        return self.position.x()

    def y(self):
        return self.position.y()

def tick(env, proj):
    position = proj.position + proj.velocity
    velocity = proj.velocity + env['gravity'] + env['wind']
    return Projectile(position, velocity)

p = Projectile(Point(0, 0, 0), Vector(1, 1.9, 0).normalize() * 10)
env = {'gravity': Vector(0, -0.1, 0), 'wind': Vector(-0.01, 0, 0)}

canvas = Canvas(900, 550)
color = Color(0.7, 0.7, 0.7)

axis_color = Color(0.1, 0.1, 0.8)
for i in range(0, 900):
    canvas.write_pixel(i, 549, axis_color)
for j in range(0, 550):
    canvas.write_pixel(0, j, axis_color)

while p.y() >= 0:
    x = round(p.x())
    y = round(550 - p.y())
    if x < 900 and y < 550 and x >= 0 and y >= 0:
        canvas.write_pixel(x, y, color)
    p = tick(env, p)

with open('output/projectile.ppm', 'w') as f:
    f.write(to_ppm_format(canvas))
