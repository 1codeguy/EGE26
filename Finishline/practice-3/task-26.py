with open(r'files/26.2_19727 (1).txt') as file:
    M, N = map(int, file.readline().split())
    cans = [int(i) for i in file]

cans = sorted(cans)

train = []
summ = 0
for can in cans:
    if summ + can <= M:
        summ += can
        train.append(can)

len_train = len(train)
summ -= train[-1]
train.remove(train[-1])
cnt = 0
for can in cans[::-1]:
    if summ + can > M:
        cnt += 1

print(len_train, cnt)