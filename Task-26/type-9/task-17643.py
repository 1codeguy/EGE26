with open(r'files/26_17643.txt') as file:
    N = int(file.readline())
    goods = [list(map(int, i.split())) for i in file]

mid_price = sum(i[1] for i in goods) / N

products = {}
for ID, price, status in goods:
    if price > mid_price:
        if ID not in products:
            products[ID] = [not status, price, status]
        else:
            products[ID] = [products[ID][0] + (not status), price, products[ID][2] + status]

keys = sorted(products, key=lambda x: (-products[x][0], -products[x][1], products[x][2]))

print(products[keys[0]][0] * products[keys[0]][1], products[keys[0]][-1])