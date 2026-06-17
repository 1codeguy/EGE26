with open(r'files/17_29349.txt') as file:
    nums = [int(i) for i in file]

min_123 = min(i for i in nums if i > 0 and i % 123 == 0)

ans = []
for pair in zip(nums, nums[1:]):
    if sum(pair) < min_123:
        ans.append(sum(pair))

print(len(ans), max(ans))