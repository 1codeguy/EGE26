from itertools import combinations

with open(r'/Users/admin/Desktop/hw3004/9.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    if max(line) < sum(line) - max(line):
        if all(num1 + num2 != num3 + num4 for num1, num2, num3, num4 in combinations(line, r=4)):
            cnt += 1

print(cnt)