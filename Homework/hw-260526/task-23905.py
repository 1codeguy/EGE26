with open(r'files/17_23905.txt') as file:
    data = [int(i) for i in file]

max_37 = max(i for i in data if i % 100 == 37)

ans = []
for nums in zip(data, data[1:], data[2:], data[3:]):
    U1 = sum(1 for i in nums if i > max_37)
    U2 = sum(1 for i in nums if i >= 10 and str(i)[-1] == str(i)[-2])
    if U1 == 2 and U2 == 1:
        ans.append(*[i for i in nums if str(i)[-1] == str(i)[-2]])

print(len(ans), sum(ans))