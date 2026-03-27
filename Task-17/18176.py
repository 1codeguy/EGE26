with open(r'.\files\17_18176.txt') as file:
    data = [int(i) for i in file]

min_4 = min(i for i in data if str(i)[-1] == '4' and i > 0)
ans = []

for num1, num2, num3 in zip(data, data[1:], data[2:]):
    if sum(map(int, str(abs(num1)))) + sum(map(int, str(abs(num2)))) + sum(map(int, str(abs(num3)))) == min_4:
        ans.append(int(num1) + int(num2) + int(num3))

print(len(ans), max(ans))