with open(r'files/17_17558.txt') as file:
    nums = [int(i) for i in file]

cnt_32 = sum(1 for i in nums if abs(i) % 32 == 0)

ans = []
for a, b in zip(nums, nums[1:]):
    U1 = (a < 0) + (b < 0)
    U2 = a + b < cnt_32
    if U1 >= 1 and U2:
        ans.append(a + b)

print(len(ans), max(ans))