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
    max = np.shape(pixel)[2]
    pixel[x,y,z] = max - z
    pixel_modif = pixel
    return pixel_modif

def bresenham3D(x1, y1, z1, x2, y2, z2, pixel): #x1,y1,z1 = point de départ, x2-1,y2-1,z2-1 = point d'arrivée
    #x lines, y columns, z depth
    e = x2-x1
    dx = e*2
    dy = (y2-y1)*2
    dz = (z2-z1)*2
    while x2 >= x1:
        tracerPixel3D(x1, y1, z1, pixel)
        x1 += 1
        e -= dy
        if e <= 0:
            y1 += 1
            e += dx
            e -= dz
            if e <= 0:
                z1 += 1
                e += dy
    return (x2,y2,z2)

def from3Dto2D(pixel):
    (y,x) = np.shape(pixel)[0:2]
    pixel2D = np.zeros((y,x), dtype=np.uint8)
    for i in range(y):
        for j in range(x):
            pixel2D[i,j] = np.max(pixel[i,j,:])
    return pixel2D

pixel1 = np.zeros((5,5,5), dtype=np.uint8)
bresenham3D(0,0,0,4,4,4,pixel1)
bresenham3D(0,0,0,4,0,4,pixel1)
pixel2D = from3Dto2D(pixel1)
print(pixel1)
print("\n")
print(pixel2D)