with open(r'files/17_27629.txt') as file:
    nums = [int(i) for i in file]

max_43 = max(i for i in nums if abs(i) % 100 == 43 and len(str(abs(i))) == 4)

ans = []
for pair in zip(nums, nums[1:]):
    U1 = any(i for i in pair if len(str(abs(i))) == 4)
    U2 = sum(pair) ** 2 < max_43 ** 2
    if U1 and U2:
        ans.append(sum(pair) ** 2)

print(len(ans), max(ans))