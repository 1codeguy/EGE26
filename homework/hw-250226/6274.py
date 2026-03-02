def f(start, end, nums=[], cnt=0):
    if start == end and cnt: return 1
    if not 40 <= start <= 49 or start in nums: return 0
    return f(start + 1, end, nums + [start], 1) + \
        f(start + 3, end, nums + [start], 1) + \
        f(start - 1, end, nums + [start], 1) + \
        f(start - 3, end, nums + [start], 1)

print(f(42, 42))