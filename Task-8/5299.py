from itertools import permutations

cnt = -1
for val in set(permutations('ХОЧУ СОТКУ')):
    val = ''.join(val)
    if val[0] not in 'У ' and val[-1] != ' '\
            and val[1] != ' ' and val[-2] != ' ':
        cnt += 1

print(cnt)