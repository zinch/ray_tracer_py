def point(x, y, z):
    return (x, y, z, 1)

def vector(x, y, z):
    return (x, y, z, 0)

def add(t1, t2):
     x1, y1, z1, w1 = t1
     x2, y2, z2, w2 = t2
     return (x1 + x2, y1 + y2, z1 + z2, w1 + w2)

