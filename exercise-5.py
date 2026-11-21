n = int(input())
a = list(map(int, input().split()))

symbols = []
for i in range(n-1):
    if (a[i] % 2 != 0) and (a[i+1] % 2 != 0):
        symbols.append(chr(120))
    else:
        symbols.append(chr(43))
        a[i+1] = a[i] + a[i+1]

print("".join(symbols))