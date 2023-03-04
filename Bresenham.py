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
        tracerPixel(x1,y1,pixel)
        x1 += 1
        e -= dy
        if e <= 0:
            y1 += 1
            e += dx
    return (x2,y2)
        

pixel = np.zeros((5,5))
tracerSegment(0,0,2,1,pixel)
print(pixel)