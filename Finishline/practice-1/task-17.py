with open(r'files/17_23376.txt') as file:
    data = [int(i) for i in file]

print(data)

max_37_2 = max(i for i in data if len(str(abs(i))) == 5 and str(i)[-2:] == '37') ** 2

ans = []
for nums in zip(data, data[1:]):
    U1 = (len(str(abs(nums[0]))) == 5) + (len(str(abs(nums[1]))) == 5)
    U2 = sum(nums) ** 2 > max_37_2
    if U2 and U1 == 1:
        ans.append(sum(nums))

print(len(ans), max(ans))