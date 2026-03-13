```
with open(r'/Users/admin/Desktop/N24/24_24977.txt') as file:
    data = file.readline()

ans = 0

for i in range(len(data) - 6):
    cnt = 0
    for j in range(i, len(data) - 6):
        if data[j] == '2' and data[j + 2] == '0' and \
                data[j + 4] == '2' and data[j + 6] == '6':
            cnt += 1
        if cnt > 10:
            ans = max(ans, len(data[i:j + 6]))
            break

print(ans)
```