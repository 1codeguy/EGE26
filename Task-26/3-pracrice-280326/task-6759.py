with open(r'/Users/admin/Desktop/N26/26_6759.txt') as file:
    N = int(file.readline())
    prods = [int(i) for i in file]

# prods = [30, 40, 50, 60, 68, 72, 80, 84, 100, 120]
# N = len(prods)
prods = sorted(prods)
sale_amount = N // 3
# store = sum(prods) - sum(prods[:sale_amount])
store = sum(prods) - sum(prods[::-1][2::3])
customer = sum(prods) - sum(prods[-sale_amount:])
print(customer, store, sum(prods))