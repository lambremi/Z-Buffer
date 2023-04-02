import numpy as np


def barycenter_calc(p1, p2, p, color1, color2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    x, y, z = p
    a = (x1-x)**2 + (y1-y)**2 + (z1-z)**2
    b = (x2-x)**2 + (y2-y)**2 + (z2-z)**2
    B = (a*color2 + b*color1) // (a + b)
    return B


def color_creation(color):
    return "#%02x%02x%02x" % (min(255,color[0]), min(255,color[1]), min(255,color[2]))


if __name__ == "__main__":
    color1 = np.array([100, 100, 100])
    color2 = np.array([255, 255, 255])
    x1, y1, z1 = 1, 0, 0
    x2, y2, z2 = 120, 0, 0

    for x in range(x1,x2+1):
        print(x, barycenter_calc(x1, y1, z1, color1, x2, y2, z2, color2, x, y1, z1))


