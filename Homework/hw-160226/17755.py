from functools import lru_cache

@lru_cache(None)
def F(n):
    if n > 400:
        return n ** n
    return n + 6 + F(n + 12)

for i in range(1, 500):
    F(i)

print(F(72) - F(108))