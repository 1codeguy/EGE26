with open(r'../files/24_4602.txt') as file:
    data = file.readline()

ans = 0
cnt = 0
i = 0
while i < len(data):
    if data[i] in 'BCD' and data[i + 1] in 'AO':
        cnt += 1
        i += 2
    else:
        ans = max(ans, cnt)
        cnt = 0
        i += 1
ans = max(ans, cnt)
print(ans)