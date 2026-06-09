with open(r'files/26_4684.txt') as file:
    N = int(file.readline())
    goods = [int(i) for i in file]

goods = sorted(goods)
price_1 = sum(goods) - sum(goods[::-1][5::6]) // 2
price_2 = sum(goods) - sum(goods[5::6]) // 2
print(price_1, price_2)