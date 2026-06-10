with open(r'files/26_6759.txt') as file:
    N = int(file.readline())
    goods = [int(i) for i in file]

goods = sorted(goods, reverse=True)

price_1 = sum(goods) - sum(goods[:N // 3])
price_2 = sum(goods) - sum(goods[2::3])
print(price_1, price_2)