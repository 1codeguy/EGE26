with open(r'files/26_6641.txt') as file:
    N, M = map(int, file.readline().split())
    goods = []
    for i in file:
        x, y = i.split()
        goods.append([int(x), y])

goods = sorted(goods, key=lambda x: (x[0], x[1]))

cnt_S = 0
bought = []
summ = 0
for good in goods:
    if summ + good[0] <= M:
        summ += good[0]
        bought.append(good)
        if good[1] == 'S':
            cnt_S += 1

len_bought = len(bought)

for cost in bought[::-1]:
    if cost[1] == 'W':
        for cost_2 in goods[len_bought:]:
            len_bought += 1
            if cost_2[1] == 'S':
                if summ - cost[0] + cost_2[0] <= M:
                    bought.remove(cost)
                    bought.append(cost_2)
                    cnt_S += 1
                    summ += -cost[0] + cost_2[0]
                    break

print(cnt_S, M - summ)
