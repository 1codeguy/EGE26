from functools import lru_cache
F = [0] * 2100
G = [0] * 304_000

for i in range(0, 303_737)[::-1]:
    if i > 303_728: G[i] = i - 15
    else: G[i] = G[i + 8] // 2 - 109

for i in range(1, 2050):
    if i >= 128: F[i] = F[i - 5] + 1092
    else: F[i] = 5 * G[i - 7] + 29

print(F[2049])

#######################

def F(n):
    if n >= 128:
        return F(n - 5) + 1092
    return 5 * G(n - 7) + 29

@lru_cache(None)
def G(n):
    if n > 303_728:
        return n - 15
    return G(n + 8) / 2 - 109

for i in range(1, 304_000)[::-1]:
    G(i)

print(F(2049))