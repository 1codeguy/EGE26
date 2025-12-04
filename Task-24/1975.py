with open(r'.\files\24_1975.txt') as file:
    data = file.readline()

test = '***P**PP****P****PP**'
ans = 0
cnt = 1
for i in range(len(data) - 1): # range(4) -> 0 1 2
    if data[i] + data[i + 1] != 'PP':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1
ans = max(ans, cnt)

print(ans)