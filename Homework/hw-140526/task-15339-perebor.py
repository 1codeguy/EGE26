with open(r'/Users/admin/Desktop/N24/24_15339.txt') as file:
    data = file.readline()

ans = 0
for i in range(len(data) - 1):
    if data[i] in 'ABC' and data[i + 1] in '6789':
        cnt = 1
        for j in range(i + 1, len(data) - 1):
            if data[j] in 'ABC' and data[j + 1] in '6789':
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 0
    if data[i] in '6789' and data[i + 1] in 'ABC':
        cnt = 1
        for j in range(i + 1, len(data) - 1):
            if data[j] in '6789' and data[j + 1] in 'ABC':
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 0
        ans = max(ans, cnt)

print(ans)