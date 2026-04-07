with open(r'/Users/admin/Desktop/Новая папка 2/17_25356.txt') as file:
    data = [int(i) for i in file]

max_30 = max(i for i in data if abs(i) % 100 == 30)
ans = []

for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = len(str(abs(num1))) != 4 and len(str(abs(num2))) != 4 and len(str(abs(num3))) != 4
    u2 = num1 + num2 + num3 > max_30
    if u1 and u2:
        ans.append(num1 + num2 + num3)

print(len(ans), max(ans))