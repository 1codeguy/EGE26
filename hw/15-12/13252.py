from itertools import permutations

cnt = 0
for val in set(permutations('КИДАЛА', r=5)):
    val = ''.join(val)
    if 'АА' not in val:
        cnt += 1

print(cnt)