with open(r'/Users/admin/Desktop/24_11813.txt') as file:
    data = file.readline()

vowels = 'AEIUY'
consonats = 'BCDFGHJKLMNPQRSTVWXYZ'

for i in vowels:
    data = data.replace(i, '+')
for i in consonats:
    data = data.replace(i, '*')

ans = 0
for i in range(len(data) - 1):
    cnt = 0
    if data[i] != data[i + 1]:
        cnt = 2
    for j in range(i + 2, len(data) - 1):
        if data[j] != data[j + 1]:
            cnt += 2
        else:
            ans = max(ans, cnt)
            break
    ans = max(ans, cnt)

print(ans)

