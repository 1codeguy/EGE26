from functools import lru_cache

@lru_cache(None)
def F(n):
    if n < 10:
        return n - 1
    if n % 2 == 0:
        return 3*n - 1 + F(n - 3)
    return 5*n + 2 + F(n - 4)

for i in range(1, 4446):
    F(i)

print(F(4445) - F(4444))