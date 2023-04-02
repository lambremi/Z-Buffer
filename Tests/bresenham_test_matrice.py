N=50
import sys
sys.path.append('../src/')
from Matrice import *

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


# def draw_matrice(window,m, n):
#     for i in range(len(m)):
#         for j in range(len(m[i])):
#             if m[i][j]!=-1:
#                 draw_pixel(window,i,j,m[i][j],n,"blue")


# def MatriceSegment2(x1, y1, z1, x2, y2, z2, m):
#     dx = abs(x1 - x2)
#     dy = abs(y1 - y2)
#     dz = abs(z2 - z1)

#     if (dx == 0):
#         m[x1][y1] = z1
#         m[x2][y2] = z2
#     else:
#         # detection de la granularité la plus fine
#         # y est la plus fine (quart sup ou inf)
#         # si point de droite a gauche, on inverse
#         if (x2 < x1):
#             xchange = x1
#             x1 = x2
#             x2 = xchange
#             ychange = y1
#             y1 = y2
#             y2 = ychange
#             zchange = z1
#             z1 = z2
#             z2 = zchange
#         # detction si on va vers y pos ou neg
#         ydeplacement = 1
#         if (y1 > y2):
#             ydeplacement = -1
#         zdeplacement = 1
#         if (z1 > z2):
#             zdeplacement = -1

#         e = x2 - x1
#         edz = x2 - x1

#         while x2 >= x1:
#             m[x1][y1] = z1
#             x1 += 1
#             e -= dy
#             edz -= dz
#             while e <= 0:
#                 y1 += ydeplacement
#                 e += dx
#             while edz <= 0:
#                 z1 += zdeplacement
#                 edz += dx


# def traceFacette( x1, y1, z1, x2, y2, z2, x3, y3, z3, m):

#     # tracage des 3 segments
#     MatriceSegment2(x1, y1, z1, x2, y2, z2, m)
#     MatriceSegment2(x3, y3, z3, x2, y2, z2, m)
#     MatriceSegment2(x1, y1, z1, x3, y3, z3, m)

#     # remplissage colone par colone
#     for h in range(N):

#         # trouver le x le plus petit, puis le plus grand
#         y1 = -1
#         y2 = -1
#         for i in range(N):
#             if (m[h][i] != -1 and y1 != -1):
#                 y2 = i
#                 z2 = m[h][i]
#             if (m[h][i] != -1 and y1 == -1):
#                 y1 = i
#                 z1 = m[h][i]
#         # remplissage y

#         zdeplacement = 1
#         if (z1 > z2):
#             zdeplacement = -1

#         if (y1 != -1 and y2 != -1):
#             dy = y2 - y1
#             dz = abs(z2 - z1)
#             e = y2 - y1
#             while y2 >= y1:
#                 m[h][y1] = z1
#                 y1 += 1
#                 e -= dz
#                 while e <= 0:
#                     z1 += zdeplacement
#                     e += dy

#     # draw_matrice(window,m,n)


# def matriceProfondeur(window, m1, m2, color, n):
#     for i in range(len(m1)):
#         for j in range(len(m1[i])):
#             if (m1[i][j] != -1 or m2[i][j] != -1):
#                 if (m1[i][j] == -1):
#                     m1[i][j] = m2[i][j]
                    
#                 elif (m1[i][j] >= m2[i][j] and m2[i][j] != -1):
#                     m1[i][j] = m2[i][j]
                   
#     return m1


matrice = [[[-1,-1] for _ in range (N)] for _ in range (N)]
matrice2 = [[-1 for _ in range (N)] for _ in range (N)]

m=[[-1 for _ in range(3)] for _ in range (3)]
liste_triangle=[[-1 for _ in range(13) ] for _ in range (100)]

#lecture matrice
file = open('3points.txt', "r")
lines =file.readlines()
i=0
compteur=0
for line in lines :
    if(line!='\n'):
        if(liste_triangle[compteur][0]==-1):
            liste_triangle[compteur][0]=line.split('\n')[0]
            i=1
        else :
            liste_triangle[compteur][i]=int(line.split(sep=' ')[0])
            liste_triangle[compteur][i+1]=int(line.split(sep=' ')[1])
            liste_triangle[compteur][i+2]=int(line.split(sep=' ')[2])
            liste_triangle[compteur][i+3]=int(line.split(sep=' ')[3])
            i+=4
        if(i==13) :
            compteur +=1
    
print (liste_triangle)
file.close()
#deter 3 points :

#matrice facette 



#ecriture matrice dans fichier
parcours = 0
test=input()
if(int(test)==0):
    file2 = open('resultat_triangle_seul.txt',"w+")
    while (liste_triangle[parcours][0]!=-1):
        p1=liste_triangle[parcours][1],liste_triangle[parcours][2],liste_triangle[parcours][3]
        p2=liste_triangle[parcours][5],liste_triangle[parcours][6],liste_triangle[parcours][7]
        p3=liste_triangle[parcours][9],liste_triangle[parcours][10],liste_triangle[parcours][11]
        color1=np.array([liste_triangle[parcours][4]]*3)
        color2=np.array([liste_triangle[parcours][8]]*3)
        color3=np.array([liste_triangle[parcours][12]]*3)

        traceFacette2_test(p1,color1,p2,color2,p3,color3,matrice)
        
        file2.write('\n\n'+liste_triangle[parcours][0]+'\n\n')
        for ligne in matrice :
            for colonne in ligne :
                if(type(colonne[1])==np.ndarray) :
                    file2.write(str(colonne[0])+' '+str(colonne[1][0])+' ')
                else : 
                    file2.write(str(colonne[0])+' '+str(colonne[1])+' ')
            file2.write('\n')
        parcours +=1
        matrice=[[[-1,-1] for _ in range (N)] for _ in range (N)]

else :
    file2 = open('resultat_2_triangle.txt',"w+")
    while (liste_triangle[parcours+1][0]!=-1):
        traceFacette(liste_triangle[parcours][1],liste_triangle[parcours][2],liste_triangle[parcours][3],liste_triangle[parcours][4],liste_triangle[parcours][5],liste_triangle[parcours][6],liste_triangle[parcours][7],liste_triangle[parcours][8],liste_triangle[parcours][9],matrice)
        traceFacette(liste_triangle[parcours+1][1],liste_triangle[parcours+1][2],liste_triangle[parcours+1][3],liste_triangle[parcours+1][4],liste_triangle[parcours+1][5],liste_triangle[parcours+1][6],liste_triangle[parcours+1][7],liste_triangle[parcours+1][8],liste_triangle[parcours+1][9],matrice2)
        matrice2=matriceProfondeur(matrice,matrice2)
        file2.write('\n\n'+liste_triangle[parcours][0]+'     '+liste_triangle[parcours+1][0]+'\n\n')
        for ligne in matrice2 :
            for colonne in ligne :
                file2.write(str(colonne)+' ')
            file2.write('\n')
        parcours +=1
        matrice=[[-1 for _ in range (N)] for _ in range (N)]
        matrice2=[[-1 for _ in range (N)] for _ in range (N)]






file2.close()