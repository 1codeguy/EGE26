with open(r'.\files\17 (2).txt') as file:
    data = [int(i) for i in file]

max_2 = max(i for i in data if 10 <= i <= 99)

ans = []
for num1, num2 in zip(data, data[1:]):
    u1 = 10 <= num1 <= 99
    u2 = 10 <= num2 <= 99
    if u1 + u2 == 1 and (num1 + num2) % max_2 == 0:
        ans.append(num1 + num2)

print(len(ans), max(ans))