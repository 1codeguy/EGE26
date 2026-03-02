def f(start, end, nums):
    nums += [start]
    if start > end: return 0
    if start == end:
        if any(sum(nums[i:i + 2]) % 11 == 0 for i in range(len(nums) - 2)):
            return 1
        return 0
    return f(start + 1, end, nums) + f(start * 3, end, nums) + f(start * 4, end, nums)

print(f(1, 600, []))