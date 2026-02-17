from functools import lru_cache

@lru_cache(None)
def F(n):
    if n < 10:
        return n
    return 3 * n + F(n - 3)

for i in range(1, 6500):
    F(i)

print((F(6250) + 2 * F(6244)) / F(6238))