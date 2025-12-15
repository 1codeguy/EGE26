from itertools import permutations

ans = []
for val in set(permutations('ПАРИЖАНКА')):
    val = ''.join(val)
    for i in val:
        if i in 'АИ':
            val = val.replace(i, '*')
    if val.count('**') == 1 and '***' not in val and '****' not in val:
        ans.append(val)

print(len(ans))gret vefgrh