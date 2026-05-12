with open(r'/Users/admin/Desktop/N24/24_4682.txt') as file:
    data = file.readline()

ans = i = 0
cnt = 1

while i < len(data):
    if data[i] in 'AE' and data[i + 1] in 'BCD':
        cnt += 1
        i += 2
    else:
        ans = max(ans, cnt)
        cnt = 1
        i += 2
ans = max(ans, cnt)

print(ans)