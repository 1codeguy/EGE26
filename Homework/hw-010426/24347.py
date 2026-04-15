from math import prod

with open(r'/Users/admin/Desktop/N26/24347.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for line in data:
    u1 = line.count(max(line)) == 1
    u2 = line[0] != max(line) and line[0] != min(line) and \
                line[-1] != max(line) and line[-1] != min(line)
    u3 = prod(sorted(line, reverse=True)[:3]) % min(line) == 0
    if u1 + u2 + u3 == 1:
        ans += 1

print(ans)