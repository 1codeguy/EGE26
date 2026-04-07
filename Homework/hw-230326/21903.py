with open(r'/Users/admin/Desktop/Новая папка 2/17_21903.txt') as file:
    data = [int(i) for i in file]

min_15 = min(i for i in data if abs(i) % 100 == 15 and 100 <= abs(i) <= 999)

ans = []
for nums in zip(data, data[1:], data[2:]):
    if min(nums) * max(nums) > min_15 ** 2:
        ans += [min(nums) * max(nums)]

print(len(ans), min(ans))