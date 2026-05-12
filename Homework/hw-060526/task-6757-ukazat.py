with open(r'/Users/admin/Desktop/N24/24_6757.txt') as file:
    data = file.readline()

ans = i = 0
cnt = 0

while i < len(data):
    if data[i:i + 3] in 'CFE FCE':
        cnt += 1
        i += 3
    else:
        ans = max(ans, cnt)
        cnt = 0
        i += 3
ans = max(ans, cnt)

print(ans)