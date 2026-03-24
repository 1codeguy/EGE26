with open(r'.\files\17522.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    if max(line) < sum(line) - max(line):
        amount = [line.count(i) for i in set(line)]
        if sorted(amount) == [1, 1, 2]:
            cnt += 1

print(cnt)