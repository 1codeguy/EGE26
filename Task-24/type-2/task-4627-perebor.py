with open(r'../files/24_4627.txt') as file:
    data = file.readline()

ans = 0
for i in range(len(data) - 2):
    if data[i:i + 3] in 'NPO PNO':
        cnt = 1
        for j in range(i + 3, len(data) - 2, 3):
            if data[j:j + 3] in 'NPO PNO':
                cnt += 1
            else:
                break
        ans = max(ans, cnt)

print(ans)