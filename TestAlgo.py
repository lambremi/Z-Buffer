from tkinter import *

p0 = (0,0)
p1 = (5,9)


N = 500     #Number of pixel
Size = 1000  #sizeWindows
n = Size/N
marge = 10

a = (p1[1] - p0[1]) / (p1[0] - p0[0])


def draw_pixel(window, x, y, z, n,color="black"):
    x1 = x*n+marge
    y1 = Size-y*n+marge
    x2 = n*(x+1)+marge
    y2 = Size-n*(y+1)+marge
    if(color == "black"):
        window.create_rectangle(x1,y1 ,x2 ,y2 , fill="#%02x%02x%02x" % (int(z), int(z), int(z)), outline="#%02x%02x%02x" % (int(z), int(z), int(z)))
    if(color == "red"):
        window.create_rectangle(x1,y1 ,x2 ,y2 , fill="#%02x0000" % int(z), outline="#%02x0000" % int(z))
    if(color == "blue"):
        window.create_rectangle(x1,y1 ,x2 ,y2 , fill="#0000%02x" % int(z), outline="#0000%02x" % int(z))
    if(color == "green"):
        window.create_rectangle(x1,y1 ,x2 ,y2 , fill="#00%02x00" % int(z), outline="#00%02x00" % int(z))
    x_center = (x1+x2)/2
    y_center = (y1+y2)/2
    #window.create_text(x_center, y_center, text=z, fill="white",font=("Helvetica", int(0.4*n)))

def draw_matrice(window,m, n):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]!=-1:
                draw_pixel(window,i,j,m[i][j],n,"blue")

def init():
    master = Tk()
    window = Canvas(master, width=(Size+2*marge), height=(Size+2*marge))
    window.pack()
    return master, window


# def tracerSegment(window, x1, y1, x2, y2, z1, z2, n): 
#     dx = abs(x1-x2)
#     dy = abs(y1-y2)
#     dz = abs(z2-z1)
    
#     if(dx ==0):
#         draw_pixel(window,x1,y1,z1,n)
#         draw_pixel(window,x2,y2,z2,n)
#     else:
#         #detection de la granularité la plus fine
#         #y est la plus fine (quart sup ou inf)
#         #si point de droite a gauche, on inverse
#         if(x2<x1):
#             xchange = x1
#             x1 = x2
#             x2 = xchange
#             ychange = y1
#             y1 = y2
#             y2 = ychange
#             zchange = z1
#             z1 = z2
#             z2 = zchange
#         #detction si on va vers y pos ou neg
#         ydeplacement = 1
#         if(y1>y2):
#             ydeplacement = -1
#         zdeplacement = 1
#         if(z1>z2):
#             zdeplacement = -1

#         e = x2-x1
#         edz = x2-x1

#         while x2 >= x1:
#             draw_pixel(window,x1,y1,z1,n)
#             x1 += 1
#             e -= dy
#             edz -= dz
#             while e <= 0 :
#                 y1 += ydeplacement
#                 e += dx
#             while edz <= 0:
#                 z1 +=zdeplacement
#                 edz += dx
  
def MatriceSegment2(x1, y1 ,z1 , x2, y2, z2, m):
    dx = abs(x1-x2)
    dy = abs(y1-y2)
    dz = abs(z2-z1)
    
    if(dx ==0):
        m[x1][y1]=z1
        m[x2][y2]=z2
    else:
        #detection de la granularité la plus fine
        #y est la plus fine (quart sup ou inf)
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
            while e <= 0 :
                y1 += ydeplacement
                e += dx
            while edz <= 0:
                z1 +=zdeplacement
                edz += dx


def traceFacette(window,x1,y1,z1,x2,y2,z2,x3,y3,z3,n,m):
    
    #tracage des 3 segments
    MatriceSegment2(x1,y1,z1,x2,y2,z2,m)
    MatriceSegment2(x3,y3,z3,x2,y2,z2,m)
    MatriceSegment2(x1,y1,z1,x3,y3,z3,m)

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

    #draw_matrice(window,m,n)

    
def matriceProfondeur(window,m1,m2,color,n):
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            if (m1[i][j]!=-1 or m2[i][j]!=-1):
                if(m1[i][j]==-1):
                    m1[i][j] = m2[i][j]
                    draw_pixel(window,i,j,m1[i][j],n,color)
                elif(m1[i][j]>=m2[i][j] and m2[i][j]!=-1):
                    m1[i][j] = m2[i][j]
                    draw_pixel(window,i,j,m1[i][j],n,color)
                    



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

     # Initialisation de la matrice
    m = [-1] * N
    for i in range(N):
        m[i] = [-1] * N
    m2 = [-1] * N
    for i in range(N):
        m2[i] = [-1] * N
    m3 = [-1] * N
    for i in range(N):
        m3[i] = [-1] * N

    a = 10

    traceFacette(window,20*a,14*a,100,2*a,45*a,4,45*a,42*a,80,n,m)
    traceFacette(window,1*a,25*a,100,5*a,46*a,4,45*a,20*a,25,n,m2)
    draw_matrice(window,m,n)
    matriceProfondeur(window,m,m2,"red",n)
    traceFacette(window,20*a,14*a,100,2*a,45*a,4,5*a,5*a,50,n,m3)
    matriceProfondeur(window,m,m3,"green",n)




    master.mainloop()

if __name__ == "__main__":
    main()


























