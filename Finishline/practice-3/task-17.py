with open(r'files/17_16383.txt') as file:
    nums = [int(i) for i in file]

max_21 = max(i for i in nums if str(i)[-2:] == '21' and len(str(abs(i))) == 5)

ans = []
for pair in zip(nums, nums[1:]):
    U1 = sum(1 for i in pair if str(i)[-2:] == '21' and len(str(abs(i))) == 5)
    U2 = sum(i * i for i in pair)
    if U1 == 1 and U2 >= max_21 ** 2:
        ans.append(sum(pair))

print(len(ans), max(ans))
