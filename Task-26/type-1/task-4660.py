with open(r'files/26_4660.txt') as file:
    N = int(file.readline())
    goods = [int(i) for i in file]

goods = sorted(goods, reverse=True)

check = 0

for i in range(0, len(goods) - 3, 4):
    s = sum(goods[i:i + 3]) + goods[i + 3] / 2
    check += s

print(check)

goods = sorted(goods)
l = len(goods) // 4
shop = sum(goods) - sum(goods[:l]) / 2

print(shop)

