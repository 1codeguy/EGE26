with open(r'/Users/admin/Desktop/17_21595.txt') as file:
    data = [int(i) for i in file]

ans = []
ch3 = [i for i in data if 1000 <= abs(i) <= 9999 and str(i)[-1] == '3']
for nums in zip(data, data[1:], data[2:]):
    if sum(nums) - min(nums) > len(ch3) ** 2:
        ans.append(sum(nums))

print(len(ans), abs(max(ans)))