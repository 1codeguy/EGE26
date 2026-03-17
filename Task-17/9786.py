with open(r'.\files\17_9786.txt') as file:
    data = [int(i) for i in file]

max_25 = max(i for i in data if str(i)[-2:] == '25')
ans = []

for num in zip(data, data[1:], data[2:]):
    u1 = sum(num) <= max_25
    cnt = sum([1 for i in num if 1000 <= abs(i) <= 9999])
    u2 = cnt <= 2
    if u1 and u2:
        ans.append(sum(num))

print(len(ans), max(ans))
