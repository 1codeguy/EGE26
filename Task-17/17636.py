with open(r'.\files\17_17636.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if i % 10 == 3 and len(str(i)) == 3)
ans = []

for num in zip(data, data[1:], data[2:]):
    u1 = any(n for n in num if abs(n) % 10 == 3 and len(str(abs(n))) == 3)
    u2 = sum(num) < maxx
    if u1 and u2:
        ans.append(sum(num))

print(len(ans), max(ans))