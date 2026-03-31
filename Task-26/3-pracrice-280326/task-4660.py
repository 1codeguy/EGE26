with open(r'/Users/admin/Desktop/N26/26_4660.txt') as file:
    N = int(file.readline())
    prods = [int(i) for i in file]

prods = sorted(prods, reverse=True)
sale_customer = 0
for i in range(3, len(prods), 4):
    sale_customer += prods[i] // 2
customer = sum(prods) - sale_customer

prods = sorted(prods)
sale_prods = N // 4
# customer = sum(prods) - sum(prods[-sale_prods:]) // 2
shop = sum(prods) - sum(prods[:sale_prods]) // 2

print(customer, shop)