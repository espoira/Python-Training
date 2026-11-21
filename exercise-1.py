P, V = map (int, input().split())
Q, M = map (int, input().split())

S = abs(V) + abs(M)
T = S - abs(P - Q)

if (2 * abs(M) < T) or (2 * abs(V) < T):
    K = 1 + 2 * max(abs(M), abs(V))
else:
    K = 2 * (S + 1)
    if T >= 0:
        K = K - (T + 1)

print(K)