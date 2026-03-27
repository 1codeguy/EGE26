with open(r'.\files\17_15333.txt') as file:
    data = [int(i) for i in file]

max_19 = max(i for i in data if i % 19 == 0)
ans = []

for num1, num2 in zip(data, data[1:]):
    u1 = num1 > max_19
    u2 = num2 > max_19
    if u1 + u2 >= 1:
        ans.append(num1 + num2)

print(len(ans), max(ans))