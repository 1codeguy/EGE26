from functools import lru_cache

@lru_cache(None)
def f(start, end, cnt=0):
    if start % 2 != 0: cnt += 1
    if start > end or cnt > 4: return 0
    if start == end: return 1
    return f(start + 2, end, cnt) + f(start + 3, end, cnt) + f(start * 2 + 1, end, cnt)

print(f(1, 625))