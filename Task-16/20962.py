from functools import lru_cache

@lru_cache(None)
def F(n):
    if n < 6:
        return n
    return (3 * n - 2) * F(n - 5)

for i in range(1, 21_000):
    F(i)

print((F(20568) - 51702 * F(20563)) / F(20553))