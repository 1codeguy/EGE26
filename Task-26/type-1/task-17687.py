with open(r'files/26_17687.txt') as file:
    N = int(file.readline())
    goods = [int(i) for i in file]

goods = sorted(goods, reverse=True)

price_1 = sum(goods) - sum(goods[:N // 9])
price_2 = sum(goods) - sum(goods[8::9])

print(price_1, price_2)