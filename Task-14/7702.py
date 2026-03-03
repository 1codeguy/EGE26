from string import printable as p

ans = []

for y in range(9, 18):
    for x in range(0, y):
        num1 = int(f'5{p[x]}{p[y]}A', 18)
        num2 = int(f'18{p[x]}7', y)
        num = num1 + num2
        ans.append(num)

print(len(set(ans)))