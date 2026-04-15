from functools import lru_cache

def F(n):
    if n >= 128: return F(n - 5) + 1092
    return 5 * G(n - 7) + 29

@lru_cache(None)
def G(n):
    if n > 303_728: return n - 15
    return G(n + 8) / 2 - 109

for i in range(304_000, 1, -1):
    G(i)

print(F(2049))
