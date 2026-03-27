with open(r'.\files\14251.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for line in data:
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 1, 1, 2, 2]:
        u2 = sum(i for i in line if line.count(i) > 1)
        u3 = sum(i for i in line if i % 2 != 0)
        if u2 <= u3:
            print(sum(line))
            break
