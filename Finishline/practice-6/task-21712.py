with open(r'files/17_21712.txt') as file:
    nums = [int(i) for i in file]

min_p_6 = min(i for i in nums if i > 0 and len(str(i)) == 4 and i % 10 == 6)

ans = []
for triple in zip(nums, nums[1:], nums[2:]):
    U1 = sum(1 for i in triple if len(str(abs(i))) == 4 and abs(i) % 10 == 6)
    if sum(triple) <= min_p_6 and U1 == 1:
        ans.append(sum(triple))

print(len(ans), max(ans))