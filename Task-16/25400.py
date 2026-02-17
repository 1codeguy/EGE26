from functools import lru_cache

@lru_cache(None)
def F(n):
    if n < 31_054: return F(n + 4) + 3020
    return 3 * (G(n - 2) - 15)


@lru_cache(None)
def G(n):
    if n >= 28: return G(n - 5) - 15
    return 3 * n - 4

for i in range(20, 32_000):
    G(i)

for i in range(32_000, 0, -1):
    F(i)

print(F(15))