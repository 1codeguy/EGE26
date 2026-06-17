with open(r'files/17_28938.txt') as file:
    nums = [int(i) for i in file]

max_28 = max(i for i in nums if abs(i) % 100 == 28)

ans = []
for triple in zip(nums, nums[1:], nums[2:]):
    U1 = any(len(str(abs(i))) == 3 for i in triple)
    SR = sum(triple) / 3
    U2 = SR > 0
    U3 = SR < max_28
    if U1 and U2 and U3:
        ans.append(sum(triple))

print(len(ans), max(ans))