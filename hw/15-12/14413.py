from itertools import permutations

cnt = 0
for val in set(permutations('СОРТИРОВКА')):
    val = ''.join(val)

    for i in val:
        if i in 'СРТВК':
            val = val.replace(i, '*')
        else:
            val = val.replace(i, '&')

    if '***' not in val and '&&&' not in val:
        cnt += 1

print(cnt)