def f(start, end, cnt=0):
    cnt += 1
    if start == end: return 1
    if start > end: return 0
    return f(start + 1, end) + f(start + 2, end) + f(start * 2, end)

for i in range(34, 60):
    print(f(1, i))