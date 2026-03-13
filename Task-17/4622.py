with open(r'.\files\17_4622.txt') as file:
    data = [int(i) for i in file]

min_19 = min(i for i in data if i > 0 and i % 19 == 0)
ans = []

for num in zip(data, data[1:]):
    if sum(num) < min_19:
        ans.append(sum(num))

print(len(ans), abs(max(ans)))