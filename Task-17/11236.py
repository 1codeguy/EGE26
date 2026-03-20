with open(r'.\files\17_11236.txt') as file:
    data = [int(i) for i in file]

min_2 = min(i for i in data if 10 <= abs(i) <= 99) ** 2
max_4 = max(i for i in data if 1000 <= abs(i) <= 9999 and str(i)[-1] == '1')
ans = []

for num1, num2, num3 in zip(data, data[1:], data[2:]):
    cnt = 0
    if num1 > min_2: cnt += 1
    if num2 > min_2: cnt += 1
    if num3 > min_2: cnt += 1
    if cnt == 2:
        if abs(num1) * abs(num2) * abs(num3) % max_4 == 0:
            ans += [abs(num1) + abs(num2) + abs(num3)]

print(len(ans), max(ans))

