with open(r'/Users/admin/Desktop/N26/26_20161.txt') as file:
    N = int(file.readline())
    prices = [list(map(int, i.split())) for i in file]

chet = sorted([price[0] for price in prices if price[1] % 2 == 0])
ne_chet = sorted([price[0] for price in prices if price[1] % 2 != 0], reverse=True)

sale_chet = 0
len_sale_chet = len(chet) * 70 // 100

for i in chet[:len_sale_chet]:
    sale_chet += i * 70 // 100
for n in chet[len_sale_chet:]:
    sale_chet += n * 80 // 100

sale_ne_chet = 0
len_sale_ne_chet = len(ne_chet) * 25 // 100

for j in ne_chet[:len_sale_ne_chet]:
    sale_ne_chet += j * 85 // 100
for x in ne_chet[len_sale_ne_chet:]:
    sale_ne_chet += x

res = sale_chet + sale_ne_chet
print(res, abs((sum(chet) - sale_chet) - (sum(ne_chet) - sale_ne_chet)))