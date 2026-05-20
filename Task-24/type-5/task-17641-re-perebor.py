from re import finditer
with open(r'/Users/admin/Desktop/N24/24_17641.txt') as file:
    data = file.readline()

num = r'(0|[1-9][0-9]*)'
pattern = rf'({num}[+*])+{num}'

matches = [match.group() for match in finditer(pattern, data)]

ans = 0

for match in matches:
    len_match = len(match)
    if eval(match) == 0:
        ans = max(ans, len_match)
    elif len_match > ans:
        for l in range(len_match - 1):
            if match[l] in '*+': continue
            if match[l] == '0' and match[l + 1] in '0123456789': continue
            for r in range(len_match - 1, l, -1):
                if match[r] in '*+': continue
                new_match = match[l:r + 1]
                if eval(new_match) == 0:
                    ans = max(ans, len(new_match))
                    break

print(ans)