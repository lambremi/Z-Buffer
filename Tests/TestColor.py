from tkinter import *
from src.Matrice import *


def init():
    master = Tk()
    window = Canvas(master, width=(Size+2*marge), height=(Size+2*marge))
    window.pack()
    return master, window


def main():
    master, window = init()

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
    p11, p12, p13, color1 = (20*a,14*a,100), (2*a,45*a,4), (45*a,42*a,80), np.array([29,17,231])
    p21, p22, p23, color2 = (1*a,25*a,100), (5*a,46*a,4), (45*a,20*a,25), np.array([27,215,215])
    p31, p32, p33, color3 = (20*a,14*a,100), (2*a,45*a,4), (5*a,5*a,50), np.array([162,17,231])

    traceFacette(window, p11, p12, p13, n, m)
    traceFacette(window, p21, p22, p23, n,m2)
    draw_matrice(window, m, n, p11, p12, p13, color1, color2, color3)



    master.mainloop()


if __name__ == "__main__":
    main()


























