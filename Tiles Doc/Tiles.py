def traceFacette2(window, p1, p2, p3, n, m):
    # tracage des 3 segments
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    x3, y3, z3 = p3

    if(x1<x2 and x1<x3):
        X1 = x1
        Y1 = y1
        Z1 = z1
        if(x2<x3):
            X2 = x2
            Y2 = y2
            Z2 = z2
            X3 = x3
            Y3 = y3
            Z3 = z3
        else:
            X2 = x3
            Y2 = y3
            Z2 = z3
            X3 = x2
            Y3 = y2
            Z3 = z2
    elif(x2<x3):
        X1 = x2
        Y1 = y2
        Z1 = z2
        if(x1<x3):
            X2 = x1
            Y2 = y1
            Z2 = z1
            X3 = x3
            Y3 = y3
            Z3 = z3
        else:
            X2 = x3
            Y2 = y3
            Z2 = z3
            X3 = x1
            Y3 = y1
            Z3 = z1
    else:
        X1 = x3
        Y1 = y3
        Z1 = z3
        if(x1<x2):
            X2 = x1
            Y2 = y1
            Z2 = z1
            X3 = x2
            Y3 = y2
            Z3 = z2
        else:
            X2 = x2
            Y2 = y2
            Z2 = z2
            X3 = x1
            Y3 = y1
            Z3 = z1


    ydeplacementLong = 1
    if (Y1 > Y3):
        ydeplacementLong = -1
    zdeplacementLong = 1
    if (Z1 > Z3):
        zdeplacementLong = -1

    ydeplacementCourt1 = 1
    if (Y1 > Y2):
        ydeplacementCourt1 = -1
    zdeplacementCourt1 = 1
    if (Z1 > Z2):
        zdeplacementCourt1 = -1

    ydeplacementCourt2 = 1
    if (Y2 > Y3):
        ydeplacementCourt2 = -1
    zdeplacementCourt2 = 1
    if (Z2 > Z3):
        zdeplacementCourt2 = -1

    edyL = X3 - X1
    edzL = X3 - X1
    edyC1 = X2 - X1
    edzC1 = X2 - X1
    edyC2 = X3 - X2
    edzC2 = X3 - X2

    dyL = abs(Y3 - Y1)*2
    dyC1 = abs(Y2 - Y1)*2
    dyC2 = abs(Y3 - Y2)*2
    dxL = abs(X3 - X1)*2
    dxC1 = abs(X2 - X1)*2
    dxC2 = abs(X3 - X2)*2
    dzL = abs(Z3 - Z1)*2
    dzC1 = abs(Z2 - Z1)*2
    dzC2 = abs(Z3 - Z2)*2

    print(X1,Y1,Z1)
    print(X2,Y2,Z2)
    print(X3,Y3,Z3)

    ZL = Z1
    ZC = Z1
    YL = Y1
    YC = Y1
    if(X1==X2):
        YC = Y2
        ZC = Z2

    while X3 >= X1:
        fillMatrice(window,X1,YL,ZL,YC,ZC,m)
        X1 += 1
        edyL -= dyL
        edzL -= dzL
        while edyL <= 0:
            YL += ydeplacementLong
            edyL += dxL
        while edzL <= 0:
            ZL += zdeplacementLong
            edzL += dxL

        if(X2 >= X1):
            print("court1")
            edyC1 -= dyC1
            edzC1 -= dzC1
            while edyC1 <= 0:
                YC += ydeplacementCourt1
                edyC1 += dxC1
            while edzC1 <= 0:
                ZC += zdeplacementCourt1
                edzC1 += dxC1
        elif(X2!=X3):
            print("court2")
            edyC2 -= dyC2
            edzC2 -= dzC2
            while edyC2 <= 0:
                YC += ydeplacementCourt2
                edyC2 += dxC2
            print("FIN1")
            while edzC2 <= 0:
                ZC += zdeplacementCourt2
                edzC2 += dxC2
            print("FIN2")

    
def fillMatrice(window,X1,YL,ZL,YC,ZC,m):
    if(YL>YC):
        YL, YC = YC, YL
        ZL, ZC = ZC, ZL
    print(X1,YL,YC,ZC,ZL)

    zdeplacement = 1
    if (ZL > ZC):
        zdeplacement = -1

    if(YL == YC):
        m[X1][YL] = ZL
    else:
        dy = YC - YL
        dz = abs(ZC - ZL)
        e = YC - YL
        while YC >= YL:
            m[X1][YL] = ZL
            YL += 1
            e -= dz
            while e <= 0:
                ZL += zdeplacement
                e += dy