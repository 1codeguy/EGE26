with open(r'/Users/admin/Desktop/26_17687.txt') as file:
    N = int(file.readline())
    prods = [int(i) for i in file]

prods = sorted(prods, reverse=True)
sale_prods = N // 9
store = sum(prods) - sum(prods[8::9])
customer = sum(prods) - sum(prods[:sale_prods])

print(customer, store)