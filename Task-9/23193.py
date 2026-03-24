with open(r'.\files\23193.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, line in enumerate(data, start=1):
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 1, 1, 3]:
        ne_pov = sum(i for i in line if line.count(i) == 1) / 3
        pov = sum(i for i in line if line.count(i) > 1) / 3
        if pov > ne_pov:
            print(pos)
