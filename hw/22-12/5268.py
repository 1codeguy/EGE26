from itertools import permutations

cnt = 0
for val in set(permutations('АМФИБРАХИЙ')):
    val = ''.join(val)
    if 'ИИФАА' in val or 'ААФИИ' in val:
        cnt += 1
print(cnt)