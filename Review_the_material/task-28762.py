with open(r'files/17_28762.txt') as file:
    nums = [int(i) for i in file]

min_23 = min(i for i in nums if i % 23 == 0)

ans = []
for pair in zip(nums, nums[1:]):
    if any(i % min_23 == 0 for i in pair):
        ans.append(sum(pair))

print(len(ans), max(ans))