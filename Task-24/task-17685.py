from re import finditer
from string import digits

with open(r'file/24_17685.txt') as file:
    data = file.readline()

n = '([1-9][0-9]*|0)'
pattern = rf'{n}([+*]{n})+'
matches = [match.group() for match in finditer(pattern, data)]

ans = 0
for m in matches:
    len_m = len(m)
    if eval(m) == 0:
        ans = max(ans, len_m)
    if len_m > ans:
        for l in range(0, len_m - 1):
            if m[l] in '+*': continue
            if m[l] == '0' and m[l + 1] not in '+*': continue
            for r in range(len_m - 1, l, -1):
                if m[r] in '+*': continue
                new_m = m[l:r + 1]
                if eval(new_m) == 0:
                    ans = max(ans, len(new_m))
                    break

print(ans)