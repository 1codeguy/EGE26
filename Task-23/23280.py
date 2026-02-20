def f(start, end):
    if start == end: return 1
    if start < end or start == 8: return 0
    return f(start - 1, end) + f(start - 4, end) + f(start // 3, end)

print(f(19, 14) * f(14, 2))