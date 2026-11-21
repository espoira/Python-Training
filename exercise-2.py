a1, a2 = map(int, input().split(":"))
b1, b2 = map(int, input().split(":"))
k = int(input())

if (a1 + b1) > (a2 + b2):
    r = 0
else:
    r = (a2 + b2) - (a1 + b1) + 1
    if (-1) ** k * (a1 - b2) > 0:
        r = r - 1
print(r)