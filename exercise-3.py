n = int(input())
a = []
k = 0
for i in range(n):
    a.append(int(input()))
    k = k + a[i] // 4 + a[i] % 4
    if a[i] % 4 == 3:
        k = k - 1
print(k)