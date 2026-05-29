from functools import lru_cache

def F(n):
    return 2 * (G(n - 3) + 8)

@lru_cache(None)
def G(n):
    if n < 10: return 2 * n
    return G(n - 2) + 1

for i in range(1, 20_000):
    G(i)

print(F(15_548))