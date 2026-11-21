n, k, d = map(int, input().split())

a = []
for i in range(d):
    j = 0

    if (n % k == 0):
        flag = False
        if not a:
            a.append(str(n))
        a.append('0')
    else:
        flag = True

    while (flag == True) and (j < 10):
        if (10 * n + j) % k == 0:
            n = 10 * n + j
            flag = False
        j = j + 1

    if (flag == True):
        print(-1)
        break

if (i == d - 1):
    if not a:
        print(n)
    else:
        print("".join(a))