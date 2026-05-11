with open(r'/Users/admin/Desktop/N24/24_4682.txt') as file:
    data = file.readline()

ans = 0
for i in range(len(data) - 1):
    if data[i] in 'AE' and data[i + 1] in 'BCD':
        cnt = 1
        for j in range(i + 2, len(data) - 1, 2):
            if data[j] in 'AE' and data[j + 1] in 'BCD':
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 1
                break

print(ans)