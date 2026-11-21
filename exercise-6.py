L, x1, v1, x2, v2 = map(int, input().split())

if (v1 == 0) and (v2 == 0):
    if (x1 == x2) or (x1 == L-x2):
        t = 0
        print("YES")
    else:
        print("NO")
        t = -1

else:
    print("YES")
    if (x1 == x2) or (x1 == L - x2):
        t = 0
    else:
        if (v1 * v2 < 0) or ((v1 - v2) * (x1 - x2) < 0 and v1 * v2 != 0) or abs(v1 - v2) == L:
            t = - (x2 - x1) / (v2 - v1)
            while (t < 0):
                t = t + abs(L / (v2 - v1))

        else:
            if (v1 + v2 > 0):
                t = - (x1 + x2) / (v1 + v2)
            else:
                t = (L - (x1 + x2)) / (v1 + v2)
            while (t < 0):
                t = t + abs(L / (v1 + v2))

if (t >= 0):
    print(format(t, ".10f"))