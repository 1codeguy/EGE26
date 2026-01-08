with open(r'17 (1).txt') as file:
    data = list(map(int, file.readlines()))

minimum = 100_000_000
for i in data:
    if i % 41 == 0 and i < minimum and i > 0:
        minimum = i

cnt = 0
ans = []
for i in range(len(data) - 1):
    if data[i] != data[i + 1] and abs(data[i] - data[i + 1]) % minimum == 0:
        cnt += 1
        ans.append(data[i] + data[i + 1])

print(max(ans), cnt)