with open(r'files/17_23276.txt') as file:
    nums = [int(i) for i in file]

max_25 = max(i for i in nums if str(i)[-2:] == '25')

ans = []
for nums in zip(nums, nums[1:], nums[2:]):
    U1 = sum(1 for i in nums if len(str(abs(i))) == 4)
    U2 = sum(nums) <= max_25
    if U1 <= 2 and U2:
        ans.append(sum(nums))

print(len(ans), max(ans))