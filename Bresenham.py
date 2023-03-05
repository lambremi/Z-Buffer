import numpy as np

def tracerPixel(y, x, pixel):
    pixel[x,y] = 255
    pixel_modif = pixel
    return pixel_modif
    
def tracerSegment(x1, y1, x2, y2, pixel): 
    e = x2-x1
    dx = e*2
    dy = (y2-y1)*2
    while x2 >= x1:
        tracerPixel(x1, y1, pixel)
        x1 += 1
        e -= dy
        if e <= 0:
            y1 += 1
            e += dx
    return (x2,y2)
        

pixel = np.zeros((5,5))
tracerSegment(0,1,4,3,pixel)
#print(pixel)

def tracerPixel3D(y, x, z, pixel):
    pixel[x,y,z] = z + 1
    pixel_modif = pixel
    return pixel_modif

def bresenham3D(x1, y1, z1, x2, y2, z2, pixel): #x1,y1,z1 = point de départ, x2-1,y2-1,z2-1 = point d'arrivée
    #x lines, y columns, z depth
    dx = x2-x1
    dy = y2-y1
    dz = z2-z1
    sx = 1 if x2>x1 else -1
    sy = 1 if y2>y1 else -1
    sz = 1 if z2>z1 else -1
    if dx >= dy and dx >= dz:
        err1 = dy
        err2 = dz
        while x1 != x2:
            tracerPixel3D(x1, y1, z1, pixel)
            err1 += dy
            err2 += dz
            if err1 >= dx:
                y1 += sy
                err1 -= dx
            if err2 >= dx:
                z1 += sz
                err2 -= dx
            x1 += sx
    elif dy >= dx and dy >= dz:
        err1 = dx
        err2 = dz
        while y1 != y2:
            tracerPixel3D(x1, y1, z1, pixel)
            err1 += dx
            err2 += dz
            if err1 >= dy:
                x1 += sx
                err1 -= dy
            if err2 >= dy:
                z1 += sz
                err2 -= dy
            y1 += sy
    else:
        err1 = dx
        err2 = dy
        while z1 != z2:
            tracerPixel3D(x1, y1, z1, pixel)
            err1 += dx
            err2 += dy
            if err1 >= dz:
                x1 += sx
                err1 -= dz
            if err2 >= dz:
                y1 += sy
                err2 -= dz
            z1 += sz
    return (x2,y2,z2)

def from3Dto2D(pixel):
    (y,x) = np.shape(pixel)[0:2]
    pixel2D = np.zeros((y,x), dtype=np.uint8)
    for i in range(y):
        for j in range(x):
            pixel2D[i,j] = np.max(pixel[i,j,:])
    return pixel2D

pixel1 = np.zeros((5,5,5), dtype=np.uint8)
bresenham3D(0,0,0,5,5,5,pixel1)
bresenham3D(3,2,0,0,4,5,pixel1)
bresenham3D(2,1,0,3,4,2,pixel1)
pixel2D = from3Dto2D(pixel1)
print(pixel1)
print("\n")
print(pixel2D)