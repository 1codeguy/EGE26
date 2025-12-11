from itertools import permutations

cnt = 0
for val in set(permutations('РОСОМАХА', r=8)):
    val = ''.join(val)
    new_val = ''
    for i in val:
        if i in 'РСМХ':
            new_val += '#'
        if i in 'ОА':
            new_val += '*'
    if '##' not in new_val and '**' not in new_val:
        cnt += 1

print(cnt)