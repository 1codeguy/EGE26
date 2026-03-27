from itertools import product

k = 0
for val in product('012345678', repeat = 4):
    val = ''.join(val)
    if val[0] != '0' and val.count('8') == 1:
        num = val.split('8')
        if sum(map(int, num[0])) == sum(map(int, num[1])):
            k += 1
print(k)
