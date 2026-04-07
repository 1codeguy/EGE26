with open(r'/Users/admin/Desktop/Новая папка 2/17_1970.txt') as file:
    data = [int(i) for i in file]

ans = []

for num1, num2 in zip(data, data[1:]):
    if abs(num1) % 3 == 0 or abs(num2) % 3 == 0:
        ans.append(num1 + num2)

print(len(ans), max(ans))