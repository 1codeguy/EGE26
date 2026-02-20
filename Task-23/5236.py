def f(start, end, nums):
    nums += [start]
    if start == end and len(nums) > 52: return 1
    if start > end: return 0
    return f(start + 2, end, nums) + f(start * 3, end, nums) + f(start * 4, end, nums)

print(f(2, 400, []))