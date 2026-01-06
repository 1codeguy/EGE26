from itertools import permutations

alph = 'КАЙФ'

cnt = 0
for val in permutations(alph, r=4):
    val = ''.join(val)
    if val[-1] != 'Й' and 'КФ' not in val:
        cnt += 1
print(cnt)