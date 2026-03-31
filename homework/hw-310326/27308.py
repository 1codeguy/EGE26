def f(start, end, flag=False):
    if start == 18 or start == 38:
        flag=True
    if start < end: return 0
    if start == end and flag: return 1
    return f(start - 3, end, flag) + f(start - 5, end, flag) + f(start // 3, end, flag)

print(f(80, 3))