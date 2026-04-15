from math import floor

with open(r'/Users/admin/Desktop/26.6_13394.txt') as file:
    N = int(file.readline())
    prods = [int(i) for i in file]

prods = sorted(prods, reverse=True)
new_prods = [i for i in prods if i > 350]

sale_prods = len(new_prods) // 3

store = sum(prods) - floor(sum(new_prods[-sale_prods:]) * .75)
customer = sum(prods) - sum(floor(i * .75) for i in new_prods[2::3])

print(customer, store)