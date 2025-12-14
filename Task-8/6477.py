from itertools import permutations

cnt = 0
for val in set(permutations('ЛЕВИОСА')):
    if val[0] not in 'ЕИОА' and val[3] not in 'ЛВС':
        cnt += 1

print(cnt)