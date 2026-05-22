from re import finditer
with open(r'/Users/admin/Desktop/N24/24_21717.txt') as file:
    data = file.readline()

pattern = r'RSQ'
starts = [match.start() for match in finditer(pattern, data)]
ends = [match.end() for match in finditer(pattern, data)]

ans = 10 ** 8

for i in range(len(starts) - 129):
    start = starts[i]
    end = ends[i + 129]
    len_line = end - start + 1
    ans = min(ans, len_line)

print(ans)

##############################################################

with open(r'..\files\24_21717.txt') as file:
    data = file.readline()

data = data.replace('RSQ', 'Rsq rsQ')
data = data.split()

ans = 10 ** 10
for i in range(len(data) - 128 - 1):
    line = ''.join(data[i:i + 129]).replace('sqrs', 'S')
    cnt = 0
    for j in data[i + 129][3:]:
        cnt += 1
        if j not in 'Qq':
            break
    ans = min(ans, len(line) + cnt)
print(ans)