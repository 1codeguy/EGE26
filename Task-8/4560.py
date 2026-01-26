from itertools import permutations

num = 0
for val in permutations('тихорецк', 4):
    val = ''.join(val)
    cnt = 0
    for i in val:
        if i in 'иое':
            cnt += 1
    if cnt == 2:
        ans = 0
        for i in range(4):
            if val[i] == 'тихо'[i]:
                ans += 1
        if ans == 2:
            num += 1
print(num)
