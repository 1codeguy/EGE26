from re import finditer

with open(r'files/24_19254.txt') as file:
    data = file.readline()

pattern = r'FSRQ'
starts = [match.start() for match in finditer(pattern, data)]
ends = [match.end() for match in finditer(pattern, data)]

ans = 0
for a, b in zip(starts, ends[81:]):
    ans = max(ans, b - a - 2)
print(ans)