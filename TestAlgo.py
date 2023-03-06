from tkinter import *

p0 = (0,0)
p1 = (5,9)


N = 50     #Number of pixel
Size = 1000  #sizeWindows
n = Size/N
marge = 10

a = (p1[1] - p0[1]) / (p1[0] - p0[0])


def draw_pixel(window, x, y, z, n):
    x1 = x*n+marge
    y1 = Size-y*n+marge
    x2 = n*(x+1)+marge
    y2 = Size-n*(y+1)+marge
    window.create_rectangle(x1,y1 ,x2 ,y2 , fill="black")
    x_center = (x1+x2)/2
    y_center = (y1+y2)/2
    window.create_text(x_center, y_center, text=z, fill="white",font=("Helvetica", int(0.4*n)))

def draw_matrice(window,m, n):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]!=-1:
                draw_pixel(window,i,j,m[i][j],n)

def init():
    master = Tk()
    window = Canvas(master, width=(Size+2*marge), height=(Size+2*marge))
    window.pack()
    return master, window


def tracerSegment(window, x1, y1, x2, y2, z1, z2, n): 
    dx = abs(x1-x2)
    dy = abs(y1-y2)
    dz = abs(z2-z1)
    
    #detection de la granularité la plus fine
    #y est la plus fine (quart sup ou inf)
    if(dy>dx):
        #si point de haut a bas, on inverse
        if(y2<y1):
            xchange = x1
            x1 = x2
            x2 = xchange
            ychange = y1
            y1 = y2
            y2 = ychange
            zchange = z1
            z1 = z2
            z2 = zchange

        #detction si on va vers x pos ou neg
        xdeplacement = 1
        if(x1>x2):
            xdeplacement = -1
        zdeplacement = 1
        if(z1>z2):
            zdeplacement = -1

        e = y2-y1
        edz = y2-y1

        while y2 >= y1:
            draw_pixel(window,x1,y1,z1,n)
            y1 += 1
            e -= dx
            edz -= dz
            if e <= 0:
                x1 += xdeplacement
                e += dy
            while edz <= 0:
                z1 +=zdeplacement
                edz += dy
                
    #x est la plus fine (quart gauche ou droit)
    else:
        #si point de droite a gauche, on inverse
        if(x2<x1):
            xchange = x1
            x1 = x2
            x2 = xchange
            ychange = y1
            y1 = y2
            y2 = ychange
            zchange = z1
            z1 = z2
            z2 = zchange
        #detction si on va vers y pos ou neg
        ydeplacement = 1
        if(y1>y2):
            ydeplacement = -1
        zdeplacement = 1
        if(z1>z2):
            zdeplacement = -1

        e = x2-x1
        edz = x2-x1

        while x2 >= x1:
            draw_pixel(window,x1,y1,z1,n)
            x1 += 1
            e -= dy
            edz -= dz
            if e <= 0:
                y1 += ydeplacement
                e += dx
            while edz <= 0:
                z1 +=zdeplacement
                edz += dx
    return (x2,y2)


def MatriceSegment(x1, y1 ,z1 , x2, y2, z2, m): 
    dx = abs(x1-x2)
    dy = abs(y1-y2)
    dz = abs(z2-z1)
    
    #detection de la granularité la plus fine
    #y est la plus fine (quart sup ou inf)
    if(dy>dx):
        #si point de haut a bas, on inverse
        if(y2<y1):
            xchange = x1
            x1 = x2
            x2 = xchange
            ychange = y1
            y1 = y2
            y2 = ychange
            zchange = z1
            z1 = z2
            z2 = zchange

        #detction si on va vers x pos ou neg
        xdeplacement = 1
        if(x1>x2):
            xdeplacement = -1
        zdeplacement = 1
        if(z1>z2):
            zdeplacement = -1

        e = y2-y1
        edz = y2-y1

        while y2 >= y1:
            m[x1][y1]=z1
            y1 += 1
            e -= dx
            edz -= dz
            if e <= 0:
                x1 += xdeplacement
                e += dy
            while edz <= 0:
                z1 +=zdeplacement
                edz += dy
                
    #y est la plus fine (quart gauche ou droit)
    else:
        #si point de droite a gauche, on inverse
        if(x2<x1):
            xchange = x1
            x1 = x2
            x2 = xchange
            ychange = y1
            y1 = y2
            y2 = ychange
            zchange = z1
            z1 = z2
            z2 = zchange
        #detction si on va vers y pos ou neg
        ydeplacement = 1
        if(y1>y2):
            ydeplacement = -1
        zdeplacement = 1
        if(z1>z2):
            zdeplacement = -1

        e = x2-x1
        edz = x2-x1

        while x2 >= x1:
            m[x1][y1]=z1
            x1 += 1
            e -= dy
            edz -= dz
            if e <= 0:
                y1 += ydeplacement
                e += dx
            while edz <= 0:
                z1 +=zdeplacement
                edz += dx
    return (x2,y2)

def traceFacette(window,x1,y1,z1,x2,y2,z2,x3,y3,z3,n):
    # Initialisation de la matrice
    m = [-1] * N
    for i in range(N):
        m[i] = [-1] * N
    
    #tracage des 3 segments
    MatriceSegment(x1,y1,z1,x2,y2,z2,m)
    MatriceSegment(x3,y3,z3,x2,y2,z2,m)
    MatriceSegment(x1,y1,z1,x3,y3,z3,m)

    #remplissage colone par colone
    for h in range(N):

        #trouver le x le plus petit, puis le plus grand
        y1 = -1
        y2 = -1
        for i in range(N):
            if(m[h][i]!=-1 and y1 != -1):
                y2 = i
                z2 = m[h][i]
            if(m[h][i]!=-1 and y1 == -1):
                y1 = i
                z1 = m[h][i]
        #remplissage y
        if(y1 != -1 and y2 != -1):
            dy = y2 - y1
            dz = z2-z1
            e = y2-y1
            while y2>=y1:
                m[h][y1] = z1
                y1 += 1
                e -= dz
                while e<=0:
                    z1 +=1
                    e +=dy

    draw_matrice(window,m,n)

    



def main():
    master, window = init()
    # draw_pixel(window, 0, 0,255, n)
    # draw_pixel(window, 9, 9,255, n)
    # draw_pixel(window, 0, 9,255, n)
    # draw_pixel(window, 9, 0,255, n)

    # tracerSegment(window,20,24,20,30,0,20,n) #1
    # tracerSegment(window,22,24,25,30,10,50,n) #2
    # tracerSegment(window,24,24,30,30,50,10,n) #3
    # tracerSegment(window,24,22,30,25,4,4,n) #4
    # tracerSegment(window,24,20,30,20,5,20,n) #5
    # tracerSegment(window,24,18,30,15,21,75,n) #6
    # tracerSegment(window,24,16,30,10,4,5,n) #7
    # tracerSegment(window,22,16,25,10,6,1,n) #8
    # tracerSegment(window,20,16,20,10,2,0,n) #9
    # tracerSegment(window,18,16,15,10,0,8,n) #10
    # tracerSegment(window,16,16,10,10,10,100,n) #11
    # tracerSegment(window,16,18,10,15,100,0,n) #12
    # tracerSegment(window,16,20,10,20,55,54,n) #13
    # tracerSegment(window,16,22,10,25,10,50,n) #14
    # tracerSegment(window,16,24,10,30,10,50,n) #15
    # tracerSegment(window,18,24,15,30,10,50,n) #16

    traceFacette(window,20,14,12,2,45,4,45,42,45,n)




    master.mainloop()

if __name__ == "__main__":
    main()


























def tracerSegment2(window, x1, y1, x2, y2, n): 
    ydeplacement = 1
    if(x2<x1):
        xchange = x1
        x1 = x2
        x2 = xchange

    if(y1>y2):
        ydeplacement = -1
        dy = (-y2+y1)*2
    else: 
        dy = (y2-y1)*2
    
    e = x2-x1
    dx = e*2
    
    while x2 >= x1:
        draw_pixel(window,x1,y1,n)
        x1 += 1
        e -= dy
        if e <= 0:
            y1 += ydeplacement
            e += dx
    return (x2,y2)