with open(r'files/17_29971.txt') as file:
    nums = [int(i) for i in file]

max_33 = max(i for i in nums if str(i)[-2:] == '33')

ans = []
for triple in zip(nums, nums[1:], nums[2:]):
    U1 = sum(1 for i in triple if len(str(abs(i))) == 2) == 2
    U2 = sum(triple) ** 2 < max_33
    if U1 and U2:
        ans.append(sum(triple))

print(len(ans), max(ans))