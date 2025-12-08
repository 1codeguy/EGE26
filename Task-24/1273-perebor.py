with open(r'/Users/admin/Desktop/24_1273.txt') as file:
    data = file.readline()

ans = 0
cnt = 2
for i in range(len(data) - 2):
    if data[i:i + 3] not in 'XYZ':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 2

ans = max(ans, cnt)
print(ans)
