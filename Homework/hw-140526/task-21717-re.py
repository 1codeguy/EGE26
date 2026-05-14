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
# using ai