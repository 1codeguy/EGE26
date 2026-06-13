from itertools import product

cnt = 0
for val in product('012345678', repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        if val.count('0') == 1:
            for i in '2468':
                val = val.replace(i, '*')
            if '*0' not in val and '0*' not in val:
                cnt += 1

print(cnt)