from itertools import permutations

ans = 0
for val in sorted(permutations('ДЖАВАСКРИПТ', r=11)):
    val = ''.join(val)
    val = val.replace('И', 'А')
    cnt = 0
    for i in range(len(val)):
        if val[i] == 'А':
            cnt += i
    if cnt == 11:
        ans += 1

print(ans)