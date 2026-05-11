with open(r'/Users/admin/Desktop/N24/24_7624.txt') as file:
    data = file.readline()

ans = i = 0
cnt = 1

while i < len(data):
    if not(data[i] in 'XYZ' and data[i + 1] in 'XYZ'):
        cnt += 1
        i += 1
    else:
        ans = max(ans, cnt)
        cnt = 1
        i += 1
ans = max(ans, cnt)

print(ans)