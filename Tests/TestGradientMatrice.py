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
    p11, p12, p13 = (20*a,14*a,100), (2*a,45*a,4), (45*a,42*a,80),
    color1, color2, color3 = np.array([29,17,231]), np.array([27,215,215]), np.array([162,17,231])

    traceFacette(window, p11, p12, p13, color1, color2, color3, n, m)
    draw_matrice(window, m, n)

    master.mainloop()


if __name__ == "__main__":
    main()


























