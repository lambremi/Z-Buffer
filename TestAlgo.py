from tkinter import *
import numpy as np
from Pixel import *
from Matrice import *


def init():
    master = Tk()
    window = Canvas(master, width=(Size+2*marge), height=(Size+2*marge))
    window.pack()
    return master, window


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
    p11, p12, p13, color1 = (20*a,14*a,100), (2*a,45*a,4), (45*a,42*a,80), np.array([255,0,0])
    p21, p22, p23, color2 = (1*a,25*a,100), (5*a,46*a,4), (45*a,20*a,25), np.array([0,255,0])
    p31, p32, p33, color3 = (20*a,14*a,100), (2*a,45*a,4), (5*a,5*a,50), np.array([0,0,255])

    traceFacette(window, p11, p12, p13, n, m)
    traceFacette(window, p21, p22, p23, n,m2)
    draw_matrice(window, m, n, p11, p12, p13, "blue")
    matriceProfondeur(window, m, m2, "red", n)
    traceFacette(window, p31, p32, p33, n, m3)
    matriceProfondeur(window, m, m3, "green", n)




    master.mainloop()


if __name__ == "__main__":
    main()


























