with open(r'.\files\17_2997.txt') as file:
    data = [int(i) for i in file]

nums_3 = [int(str(abs(i))[1]) for i in data if len(str(abs(i))) == 3]
moda = max((nums_3.count(i), i) for i in range(10))[1]
ans = []

for nums in zip(data, data[1:]):
    if any(i for i in nums if abs(i) % 10 == moda):
        ans += [sum(nums)]

print(len(ans), max(ans))