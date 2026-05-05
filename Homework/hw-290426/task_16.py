from functools import lru_cache

@lru_cache(None)
def F(n):
    if n < 10: return 1
    return (n + 3) * F(n - 3)

for i in range(1, 250_000):
    F(i)

print((F(247_563) / 519 - 477 * F(247_560)) / F(247_557))
