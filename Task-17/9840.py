with open(r'.\files\17_9840.txt') as file:
    data = [int(i) for i in file]

max_39 = max(i for i in data if 1000 <= abs(i) <= 9999 and str(i)[-2:] == '39')
ans = []

for num in zip(data, data[1:]):
    cnt_4 = [n for n in num if 1000 <= abs(n) <= 9999]
    u1 = len(cnt_4) == 1
    u2 = sum(num) ** 2 <= max_39 ** 2
    if u1 and u2:
        ans.append(sum(num))

print(len(ans), max(ans))