def f(start, end, cnt=0):
    if start in range(24, 32): cnt += 1
    if start > end or cnt > 1: return 0
    if start == end and cnt == 1: return 1
    return f(start + 1, end) + f(start + 2, end) + f(start + 4, end) + f(start + 8, end)

print(f(16, 48))