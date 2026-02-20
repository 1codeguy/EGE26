from functools import lru_cache

@lru_cache(None)
def F(n):
    if n >= 2025: return n
    return F(n + 1) - F(n + 2) + 7

for i in range(3000, 1, -1):
    F(i)

print(F(15) - F(24))

#######################

ans = [0] * 2030
ans[2026] = 2026
ans[2025] = 2025
for i in range(2024, 0, -1):
    ans[i] = ans[i + 1] - ans[i + 2] + 7

print(ans[15] - ans[24])

