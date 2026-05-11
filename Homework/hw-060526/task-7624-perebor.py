with open(r'/Users/admin/Desktop/N24/24_7624.txt') as file:
    data = file.readline()

ans = 0
for i in range(len(data) - 1):
    if not(data[i] in 'XYZ' and data[i + 1] in 'XYZ'):
        cnt = 1
        for j in range(i + 1, len(data) - 1):
            if not(data[j] in 'XYZ' and data[j + 1] in 'XYZ'):
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 1
                break

print(ans)