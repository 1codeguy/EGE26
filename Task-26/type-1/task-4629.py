with open(r'files/26_4629.txt') as file:
    N = int(file.readline())
    goods = [int(i) for i in file]


goods = sorted(goods, reverse=True)
l = len(goods) // 4

price_1 = sum(goods) - sum(goods[:l]) / 2

goods = goods[::-1]
price_2 = sum(goods) - sum(goods[:l]) / 2

print(price_1, price_2)