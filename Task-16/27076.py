from functools import lru_cache

@lru_cache(None)
def F(n):
    if n < 43:
        return G(n + 4)
    return 2 * F(n - 2) - F(n - 4) + 2

@lru_cache(None)
def G(n):
    if n < 11_240:
        return G(n + 3) + 2
    return Q(n)

@lru_cache(None)
def Q(n):
    if n < 21:
        return n + 4
    return Q(n - 4) + 2

for i in range(21, 11_240):
    Q(i)

for i in range(11_240, 46, -1):
    G(i)

print(F(2026))

############################
Q = [0] * 12_001
for i in range(12_001):
    if i < 21: Q[i] = i + 4
    else: Q[i] = Q[i - 4] + 2

G = [0] * 12_001
for i in range(12_000, 0, -1):
    if i < 11_240: G[i] = G[i + 3] + 2
    else: G[i] = Q[i]

F = [0] * 3000
for i in range(2000):
    if i < 43: F[i] = G[i + 4]
    else: F[i] = 2 * F[i - 2] - F[i - 4] + 2

print(F[2026])