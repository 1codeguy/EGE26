from itertools import combinations

with open(r'.\files\17_5758.txt') as file:
    data = [int(i) for i in file]

moda = max((data.count(i), i) for i in data)
ans = []

for num1, num2 in combinations(data, 2):
    if num1 < moda[1] < num2 and (num1 - num2 - 1) % 2 != 0:
        ans.append(abs(moda[1] - max(num1, num2)))

print(len(ans), max(ans))