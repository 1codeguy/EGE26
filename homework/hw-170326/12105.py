from functools import lru_cache

@lru_cache(None)
def F(n):
    if n <= 5: return n
    return 2 * n - 8 + F(n - 2) + F(n - 1) // 8

for i in range(1, 170):
    F(i)

print(F(163))