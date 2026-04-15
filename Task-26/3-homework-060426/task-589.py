with open(r'/Users/admin/Desktop/26_589.txt') as file:
    N = int(file.readline())
    prods = [int(i) for i in file]

prods = sorted(prods)
bunches = []
bunch = [prods[0]]
maxi = 501

for i in prods[1:]:
    if i < maxi:
        bunch += [i]
    else:
        bunches += [sorted(bunch, reverse=True)]
        bunch = []
        maxi += 500

bunches = sorted(bunches, reverse=True)

sale_max_prod = len(bunches[0]) // 2
max_prod = bunches[0][-sale_max_prod:][0] // 2

sale_sum = 0
for bunch in bunches:
    sale_bunch = len(bunch) // 2
    sale_sum += sum(bunch[-sale_bunch:]) // 2

print(sale_sum, max_prod)
