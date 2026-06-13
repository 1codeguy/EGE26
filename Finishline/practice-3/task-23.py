def func_1(start, end):
    if start > end or start == 60: return 0
    if start == end: return 1
    return func_1(start + 1, end) + func_1(start * 2, end) + func_1(start * 3, end)

def func_2(start, end):
    if start > end or start == 30: return 0
    if start == end: return 1
    return func_2(start + 1, end) + func_2(start * 2, end) + func_2(start * 3, end)

res_1 = func_1(10, 30) * func_1(30, 70)
res_2 = func_2(10, 60) * func_2(60, 70)

print(res_1 + res_2)

