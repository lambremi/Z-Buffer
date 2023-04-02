from tkinter import *
import sys
sys.path.append('../src/')
from Matrice import *
from random import randint

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

    m = [[[-1, -1] for _ in range(N)] for _ in range(N)]

    # MatriceSegment2(20,24,1,20,30,1,m) #1
    # MatriceSegment2(22,24,1,25,30,1,m) #2
    # MatriceSegment2(24,24,1,30,30,1,m) #3
    # MatriceSegment2(24,22,1,30,25,1,m) #4
    # MatriceSegment2(24,20,1,30,20,1,m) #5
    # MatriceSegment2(24,18,1,30,15,1,m) #6
    # MatriceSegment2(24,16,1,30,10,1,m) #7
    # MatriceSegment2(22,16,1,25,10,1,m) #8
    # MatriceSegment2(20,16,1,20,10,1,m) #10
    # MatriceSegment2(18,16,1,15,10,1,m) #11
    # MatriceSegment2(16,16,1,10,10,1,m) #9
    # MatriceSegment2(16,18,1,10,15,1,m) #12
    # MatriceSegment2(16,20,1,10,20,1,m) #13
    # MatriceSegment2(16,22,1,10,25,1,m) #14
    # MatriceSegment2(16,24,1,10,30,1,m) #15
    # MatriceSegment2(18,24,1,15,30,1,m) #16


    a = 10
    p11, p12, p13 = (randint(0, N // a - 1) * a, randint(0, N // a - 1) * a, randint(0, N // a - 1)), (randint(0, N // a - 1) * a, randint(0, N // a - 1) * a, randint(0, N // a - 1)), (randint(0, N // a - 1) * a, randint(0, N // a - 1) * a, randint(0, N // a - 1))
    color1, color2, color3 = np.array([randint(0, 255), randint(0, 255), randint(0, 255)]), np.array([randint(0, 255), randint(0, 255), randint(0, 255)]), np.array([randint(0, 255), randint(0, 255), randint(0, 255)])
    # color1, color2, color3 = np.array([randint(0,255)]*3), np.array([randint(0,255)]*3), np.array([randint(0,255)]*3)

    # p11, p12, p13 = (440, 150, 4) , (60, 90, 11) , (280, 280, 35)
    # color1, color2, color3 = np.array ( [ 9 , 235 , 72 ] ) , np.array ( [ 171 , 219 , 88 ] ) , np.array ( [ 155 , 159 , 219 ] )

    print(p11, ',', p12, ',', p13)
    print('np.array ( [', color1[0], ',', color1[1], ',', color1[2], '] ) ,', 'np.array ( [', color2[0], ',', color2[1], ',', color2[2], '] ) ,', 'np.array ( [', color3[0], ',', color3[1], ',', color3[2], '] )')

    traceFacette2(window, p11, color1, p12, color2, p13, color3, n, m)
    draw_matrice(window, m, n)

    x1, y1, z1 = p11
    draw_pixel(window,x1,y1,z1, n, "red")
    x1, y1, z1 = p12
    draw_pixel(window,x1,y1,z1, n, "red")
    x1, y1, z1 = p13
    draw_pixel(window,x1,y1,z1, n, "red")




    master.mainloop()


if __name__ == "__main__":
    main()


























