with open(r'/Users/admin/Desktop/N26/26_4629.txt') as file:
    N = int(file.readline())
    prods = [int(i) for i in file]

prods = sorted(prods)
sale_prods = N // 4

customer = sum(prods) - sum(prods[-sale_prods:]) // 2
store = sum(prods) - sum(prods[:sale_prods]) // 2

print(customer, store)
