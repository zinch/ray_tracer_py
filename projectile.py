from core.geom import Point, Vector

class Projectile:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def x(self):
        return self.position.t[0]

    def y(self):
        return self.position.t[1]

def tick(env, proj):
    position = proj.position + proj.velocity
    velocity = proj.velocity + env['gravity'] + env['wind']
    return Projectile(position, velocity)

p = Projectile(Point(0, 1, 0), Vector(1, 1, 0).normalize())
env = {'gravity': Vector(0, -0.1, 0), 'wind': Vector(-0.01, 0, 0)}

while p.y() >= 0:
    print(f'({round(p.x(), 2)}, {round(p.y(), 2)})')
    p = tick(env, p)
