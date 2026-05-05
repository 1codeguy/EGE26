def f(start, end):
    if start > end or start == 14: return False
    if start == end: return True
    return f(start + 1, end) + f(start * 2, end) + f(start * 3, end)

print(f(2, 39))