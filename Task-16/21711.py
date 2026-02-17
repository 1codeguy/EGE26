from functools import lru_cache

@lru_cache(None)
def F(n):
    if n < 20:
        return n
    return (n - 6) * F(n - 7)

for i in range(1, 50_000):
    F(i)

print((F(47872) - 290 * F(47865)) / F(47858))