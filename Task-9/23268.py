with open(r'.\files\23268.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, line in enumerate(data, start=1):
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 1, 1, 2, 2]:
        pov = sum(i for i in line if line.count(i) > 1) / 4
        max_ne_pov = max(i for i in line if line.count(i) == 1)
        if pov < max_ne_pov:
            print(pos)
            break