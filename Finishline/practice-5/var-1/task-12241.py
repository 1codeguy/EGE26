with open(r'files/9.txt') as file:
    lines = [list(map(int, i.split())) for i in file]

cnt = 0
for line in lines:
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 2, 2, 2]:
        pov = [i for i in line if line.count(i) > 1]
        ne_pov = sum(i for i in line if line.count(i) == 1)
        mid = (max(pov) + min(pov)) / 2
        if mid < ne_pov:
            cnt += 1

print(cnt)