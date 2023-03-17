import numpy as np


def traceFacette2(window, p1, color1, p2, color2, p3, color3, n, m):
    # tracage des 3 segments
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    x3, y3, z3 = p3
    c1, c2, c3 = np.copy(color1), np.copy(color2), np.copy(color3)

    if (x1 < x2 and x1 < x3):
        X1 = x1
        Y1 = y1
        Z1 = z1
        C1 = c1
        if (x2 < x3):
            X2 = x2
            Y2 = y2
            Z2 = z2
            C2 = c2
            X3 = x3
            Y3 = y3
            Z3 = z3
            C3 = c3
        else:
            X2 = x3
            Y2 = y3
            Z2 = z3
            C2 = c3
            X3 = x2
            Y3 = y2
            Z3 = z2
            C3 = c2
    elif (x2 < x3):
        X1 = x2
        Y1 = y2
        Z1 = z2
        C1 = c2
        if (x1 < x3):
            X2 = x1
            Y2 = y1
            Z2 = z1
            C2 = c1
            X3 = x3
            Y3 = y3
            Z3 = z3
            C3 = c3
        else:
            X2 = x3
            Y2 = y3
            Z2 = z3
            C2 = c3
            X3 = x1
            Y3 = y1
            Z3 = z1
            C3 = c1
    else:
        X1 = x3
        Y1 = y3
        Z1 = z3
        C1 = c3
        if (x1 < x2):
            X2 = x1
            Y2 = y1
            Z2 = z1
            C2 = c1
            X3 = x2
            Y3 = y2
            Z3 = z2
            C3 = c2
        else:
            X2 = x2
            Y2 = y2
            Z2 = z2
            C2 = c2
            X3 = x1
            Y3 = y1
            Z3 = z1
            C3 = c1

    ydeplacementLong = 1
    if (Y1 > Y3):
        ydeplacementLong = -1
    zdeplacementLong = 1
    if (Z1 > Z3):
        zdeplacementLong = -1
    cdeplacementLong = np.array([1] * 3)
    for i in range(3):
        if (C1[i] > C3[i]):
            cdeplacementLong[i] = -1

    ydeplacementCourt1 = 1
    if (Y1 > Y2):
        ydeplacementCourt1 = -1
    zdeplacementCourt1 = 1
    if (Z1 > Z2):
        zdeplacementCourt1 = -1
    cdeplacementCourt1 = np.array([1] * 3)
    for i in range(3):
        if (C1[i] > C2[i]):
            cdeplacementCourt1[i] = -1

    ydeplacementCourt2 = 1
    if (Y2 > Y3):
        ydeplacementCourt2 = -1
    zdeplacementCourt2 = 1
    if (Z2 > Z3):
        zdeplacementCourt2 = -1
    cdeplacementCourt2 = np.array([1] * 3)
    for i in range(3):
        if (C2[i] > C3[i]):
            cdeplacementCourt2[i] = -1

    edyL = X3 - X1
    edzL = X3 - X1
    edcL = np.array([X3 - X1] * 3)
    edyC1 = X2 - X1
    edzC1 = X2 - X1
    edcC1 = np.array([X2 - X1] * 3)
    edyC2 = X3 - X2
    edzC2 = X3 - X2
    edcC2 = np.array([X3 - X2] * 3)

    dyL = abs(Y3 - Y1) * 2
    dyC1 = abs(Y2 - Y1) * 2
    dyC2 = abs(Y3 - Y2) * 2
    dxL = abs(X3 - X1) * 2
    dxC1 = abs(X2 - X1) * 2
    dxC2 = abs(X3 - X2) * 2
    dzL = abs(Z3 - Z1) * 2
    dzC1 = abs(Z2 - Z1) * 2
    dzC2 = abs(Z3 - Z2) * 2
    dcL = abs(C3 - C1) * 2
    dcC1 = abs(C2 - C1) * 2
    dcC2 = abs(C3 - C2) * 2

    print(X1, Y1, Z1, C1)
    print(X2, Y2, Z2, C2)
    print(X3, Y3, Z3, C3)

    ZL = Z1
    ZC = Z1
    YL = Y1
    YC = Y1
    CL = np.copy(C1)
    CC = np.copy(C1)
    if (X1 == X2):
        YC = Y2
        ZC = Z2
        CC = np.copy(C2)

    while X3 >= X1:
        fillMatrice(window, X1, YL, ZL, np.copy(CL), YC, ZC, np.copy(CC), m)
        X1 += 1
        edyL -= dyL
        edzL -= dzL
        edcL -= dcL
        while edyL <= 0 and dxL != 0:
            YL += ydeplacementLong
            edyL += dxL
        while edzL <= 0 and dxL != 0:
            ZL += zdeplacementLong
            edzL += dxL
        for i in range(3):
            while edcL[i] <= 0 and dxL != 0:
                CL[i] += cdeplacementLong[i]
                edcL[i] += dxL

        if (X2 >= X1):
            print("court1")
            edyC1 -= dyC1
            edzC1 -= dzC1
            edcC1 -= dcC1
            while edyC1 <= 0:
                YC += ydeplacementCourt1
                edyC1 += dxC1
            while edzC1 <= 0:
                ZC += zdeplacementCourt1
                edzC1 += dxC1
            for i in range(3):
                while edcC1[i] <= 0:
                    CC[i] += cdeplacementCourt1[i]

        elif (X2 != X3):
            print("court2")
            edyC2 -= dyC2
            edzC2 -= dzC2
            edcC2 -= dcC2
            while edyC2 <= 0:
                YC += ydeplacementCourt2
                edyC2 += dxC2
            print("FIN1")
            while edzC2 <= 0:
                ZC += zdeplacementCourt2
                edzC2 += dxC2
            print("FIN2")
            for i in range(3):
                while edcC2[i] <= 0:
                    CC[i] += cdeplacementCourt2[i]
                    edcC2[i] += dxC2
                print("FIN{}".format(i + 3))


def fillMatrice(window, X1, YL, ZL, CL, YC, ZC, CC, m):
    if (YL > YC):
        YL, YC = YC, YL
        ZL, ZC = ZC, ZL
        CL, CC = CC, CL
    print(X1, YL, YC, ZC, ZL, CC, CL)

    zdeplacement = 1
    if (ZL > ZC):
        zdeplacement = -1

    cdeplacement = np.array([1] * 3)
    for i in range(3):
        if (CL[i] > CC[i]):
            cdeplacement[i] = -1

    if (YL == YC):
        m[X1][YL][0] = ZL
        m[X1][YL][1] = np.copy(CL)
    else:
        dy = YC - YL
        dz = abs(ZC - ZL)
        dc = abs(CC - CL)
        e = YC - YL
        ec = np.array([YC - YL] * 3)
        while YC >= YL:
            m[X1][YL][0] = ZL
            m[X1][YL][1] = np.copy(CL)
            YL += 1
            e -= dz
            ec -= dc
            while e <= 0:
                ZL += zdeplacement
                e += dy
            for i in range(3):
                while ec[i] <= 0:
                    CL[i] += cdeplacement[i]
                    ec[i] += dy
