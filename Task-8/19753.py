from itertools import permutations
from string import printable as sevatop

cnt = 0
for val in permutations(sevatop[:10], r=6):
    if val[0] != '0':
        val = ''.join(val)
        if int(val) % 4 == 0:
            for i in range(len(val) - 1):
                if int(val[i]) % 2 == 0 and \
                        int(val[i + 1]) % 2 == 0:
                    break
            else:
                cnt += 1
print(cnt)