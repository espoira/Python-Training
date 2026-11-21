cells = int(input())
x = []
y = []
P = 0

for i in range(cells):
    coords = list(map(int, input().split()))
    x.append(coords[0])
    y.append(coords[1])

for i in range(len(x)):
    P = P + 4
    for j in range(i, len(x)):
        if (x[j] == x[i]):
            if abs(y[j] - y[i]) == 1:
                P = P - 2

        if (y[j] == y[i]):
            if abs(x[j] - x[i]) == 1:
                P = P - 2

print(P)