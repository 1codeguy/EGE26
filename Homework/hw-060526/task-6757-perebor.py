with open(r'/Users/admin/Desktop/N24/24_6757.txt') as file:
    data = file.readline()

ans = 0
for i in range(len(data) - 2):
    if data[i:i + 3] in 'CFE FCE':
        cnt = 1
        for j in range(i + 3, len(data) - 2, 3):
            if data[j:j + 3] in 'CFE FCE':
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 1
                break

print(ans)