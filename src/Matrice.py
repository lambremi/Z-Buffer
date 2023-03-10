from src.Pixel import *
from src.Color import *


# def tracerSegment(window, x1, y1, x2, y2, z1, z2, n):
#     dx = abs(x1-x2)
#     dy = abs(y1-y2)
#     dz = abs(z2-z1)

#     if(dx ==0):
#         draw_pixel(window,x1,y1,z1,n)
#         draw_pixel(window,x2,y2,z2,n)
#     else:
#         #detection de la granularite la plus fine
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


def draw_matrice(window,m, n, p1, p2, p3, color1=None, color2=None, color3=None):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] != -1:
                p = (i, j, m[i][j])
                if type(color1) == np.ndarray and type(color2) == np.ndarray:
                    # b is the barycenter of (p1, color1) and (p2, color2)
                    b = barycenter_calc(p1, p2, p, color1, color2)
                    if type(color3) == np.ndarray:
                        # pb is the geometrical barycenter of p1 and p2
                        pb = ((p1[0]+p2[0])//2, (p1[1]+p2[1])//2, (p1[2]+p2[2])//2)
                        # b becomes the barycenter of (pb, b) and (p3, color3)
                        b = barycenter_calc(p3, pb, p, color3, b)
                    # creation of a string which represents an RGB code
                    color = color_creation(b)
                elif type(color1) != np.ndarray:
                    color = color1
                else:
                    color = "black"
                draw_pixel(window, i, j, m[i][j], n, color)


def MatriceSegment2(x1, y1, z1, x2, y2, z2, m):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    dz = abs(z1 - z2)

    if (dx == 0):
        m[x1][y1] = z1
        m[x2][y2] = z2
    else:
        # detection de la granularité la plus fine
        # y est la plus fine (quart sup ou inf)
        # si point de droite a gauche, on inverse
        if (x2 < x1):
            xchange = x1
            x1 = x2
            x2 = xchange
            ychange = y1
            y1 = y2
            y2 = ychange
            zchange = z1
            z1 = z2
            z2 = zchange
        # detection si on va vers y pos ou neg
        ydeplacement = 1
        if (y1 > y2):
            ydeplacement = -1
        zdeplacement = 1
        if (z1 > z2):
            zdeplacement = -1

        e = x2 - x1
        edz = x2 - x1

        while x2 >= x1:
            m[x1][y1] = z1
            x1 += 1
            e -= dy
            edz -= dz
            while e <= 0:
                y1 += ydeplacement
                e += dx
            while edz <= 0:
                z1 += zdeplacement
                edz += dx


def traceFacette(window, p1, p2, p3, n, m):
    # tracage des 3 segments
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    x3, y3, z3 = p3
    MatriceSegment2(x1, y1, z1, x2, y2, z2, m)
    MatriceSegment2(x3, y3, z3, x2, y2, z2, m)
    MatriceSegment2(x1, y1, z1, x3, y3, z3, m)

    # remplissage colone par colone
    for h in range(N):

        # trouver le x le plus petit, puis le plus grand
        y1 = -1
        y2 = -1
        for i in range(N):
            if (m[h][i] != -1 and y1 != -1):
                y2 = i
                z2 = m[h][i]
            if (m[h][i] != -1 and y1 == -1):
                y1 = i
                z1 = m[h][i]
        # remplissage y
        if (y1 != -1 and y2 != -1):
            dy = y2 - y1
            dz = z2 - z1
            e = y2 - y1
            while y2 >= y1:
                m[h][y1] = z1
                y1 += 1
                e -= dz
                while e <= 0:
                    z1 += 1
                    e += dy

    # draw_matrice(window,m,n)


def matriceProfondeur(window, m1, m2, color, n):
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            if (m1[i][j] != -1 or m2[i][j] != -1):
                if (m1[i][j] == -1):
                    m1[i][j] = m2[i][j]
                    draw_pixel(window, i, j, m1[i][j], n, color)
                elif (m1[i][j] >= m2[i][j] and m2[i][j] != -1):
                    m1[i][j] = m2[i][j]
                    draw_pixel(window, i, j, m1[i][j], n, color)