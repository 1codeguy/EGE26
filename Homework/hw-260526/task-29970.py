from functools import lru_cache

def F(n):
    return 3 * G(n - 3) + 7

@lru_cache(None)
def G(n):
    if n <= 20: return n + 2
    return G(n - 3) + 1

for i in range(10, 100_000):
    G(i)

print(F(37_811))