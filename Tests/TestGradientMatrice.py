from random import randint
from tkinter import *
import numpy as np
from src.GradientMatrice import *


def init():
    master = Tk()
    window = Canvas(master, width=(Size+2*marge), height=(Size+2*marge))
    window.pack()
    return master, window


def main():
    master, window = init()

     # Initialisation de la matrice
    m = [[[-1, -1] for _ in range(N)] for _ in range(N)]

    a = 10
    p11, p12, p13 = (randint(0,N//a-1)*a,randint(0,N//a-1)*a,randint(0,N//a-1)), (randint(0,N//a-1)*a,randint(0,N//a-1)*a,randint(0,N//a-1)), (randint(0,N//a-1)*a,randint(0,N//a-1)*a,randint(0,N//a-1))
    color1, color2, color3 = np.array([randint(0,255),randint(0,255),randint(0,255)]), np.array([randint(0,255),randint(0,255),randint(0,255)]), np.array([randint(0,255),randint(0,255),randint(0,255)])
    # color1, color2, color3 = np.array([randint(0,255)]*3), np.array([randint(0,255)]*3), np.array([randint(0,255)]*3)

    #p11, p12, p13 = (440, 150, 4) , (60, 90, 11) , (280, 280, 35)
    #color1, color2, color3 = np.array ( [ 9 , 235 , 72 ] ) , np.array ( [ 171 , 219 , 88 ] ) , np.array ( [ 155 , 159 , 219 ] )

    print(p11, ',', p12, ',', p13)
    print('np.array ( [', color1[0], ',', color1[1], ',', color1[2], '] ) ,', 'np.array ( [', color2[0], ',', color2[1], ',', color2[2], '] ) ,', 'np.array ( [', color3[0], ',', color3[1], ',', color3[2], '] )')

    traceFacette(window, p11, p12, p13, color1, color2, color3, n, m)
    draw_matrice(window, m, n)

    master.mainloop()


if __name__ == "__main__":
    main()


























