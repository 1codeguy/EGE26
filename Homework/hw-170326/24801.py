from functools import lru_cache

@lru_cache(None)
def f(start, end, flag=False):
    if start in {24, 32}: flag = not flag
    if start > end or start > 33 and not flag: return 0
    if start == end and flag: return 1
    return f(start + 1, end, flag) + \
        f(start + 2, end, flag) + \
        f(start + 4, end, flag) + \
        f(start + 8, end, flag)

for i in range(16, 48):
    f(i, 48)

print(f(16, 48))