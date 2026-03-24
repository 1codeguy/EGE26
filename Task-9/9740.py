with open(r'.\files\9740.txt') as file:
    data = [list(map(int, i.split()))for i in file]

cnt = 0
for line in data:
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 1, 1, 1, 3]:
        mid = sum(i for i in line if line.count(i) == 1) / 4
        pov = sum(i for i in line if line.count(i) > 1) / 3
        if mid <= pov:
            cnt += 1

print(cnt)