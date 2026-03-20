with open(r'.\files\17_23902.txt') as file:
    data = [int(i) for i in file]

ans = []

for nums in zip(data, data[1:], data[2:]):
    u1 = str(nums[0])[0] == str(nums[0])[-1]
    u2 = str(nums[1])[0] == str(nums[1])[-1]
    u3 = str(nums[2])[0] == str(nums[2])[-1]
    if u1 + u2 + u3 == 1:
        if len([num for num in nums if 1000 <= num <= 9999 and num % 1000 // 100 == 2]) == 2:
            ans.append(max(nums))

print(len(ans), sum(ans))