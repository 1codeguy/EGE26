from itertools import permutations

cnt = 0
for val in set(permutations('АМФИБРАХИЙ')):
    val = ''.join(val)
    if val[4] + val[5] == 'БР':
        cnt += 1

print(cnt)