with open(r'.\files\17_17558.txt') as file:
    data = [int(i) for i in file]

cnt_32 = sum(1 for i in data if i % 32 == 0)
ans = []

for num1, num2 in zip(data, data[1:]):
    u1 = num1 < 0 or num2 < 0
    u2 = num1 + num2 < cnt_32
    if u1 and u2:
        ans.append(num1 + num2)

print(len(ans), max(ans))