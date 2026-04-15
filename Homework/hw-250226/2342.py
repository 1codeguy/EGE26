def f(start, end):
    if start == end: return 1
    if start > end: return 0
    if start % 10 == 9:
        return f(start + 1, end) + f(start + 10, end)
    return f(start + 1, end) + f(start + 11, end)

print(f(25, 51))