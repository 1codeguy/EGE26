from functools import lru_cache

@lru_cache(None)
def F(n):
    if n < 2010:
        return F(n + 3) + F(n + 2) + F(n + 1)
    return n

for i in range(1, 2020):
    F(i)

print((F(2000) - 2 * (F(2002) + F(2003))) / F(2004))