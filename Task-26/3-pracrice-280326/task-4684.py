with open(r'/Users/admin/Desktop/N26/26_4684.txt') as file:
    N = int(file.readline())
    prods = [int(i) for i in file]

prods = sorted(prods)
sale_prods = N // 6
store = sum(prods) - sum(prods[:sale_prods]) // 2
customer = sum(prods) - sum(prods[::-1][5::6]) // 2

print(customer, store)