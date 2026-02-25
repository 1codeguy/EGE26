def f(start, k):
    if k == 8:
        if start in range(1000, 1025): return {start}
        return set()
    return f(start + 1, k + 1) | f(start + 5, k + 1) | f(start * 3, k + 1)

print(len(f(1, 0)))