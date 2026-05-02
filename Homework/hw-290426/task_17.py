with open(r'/Users/admin/Downloads/Inf_1_ege2026/Доп. файлы_ИНФ/1_17.txt') as file:
    data = [int(i) for i in file]

min_123 = min(i for i in data if i > 0 and i % 123 == 0)

cnt = 0
for num1, num2 in zip(data, data[1:]):
    if num1 + num2 < min_123:
        cnt += 1

print(cnt)