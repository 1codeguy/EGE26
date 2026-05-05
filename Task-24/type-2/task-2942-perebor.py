with open(r'../files/24_2942.txt') as file:
    data = file.readline()

ans = 0
cnt = 0
for i in range(0, len(data) - 1, 2):
    if data[i] + data[i + 1] in 'AB AC':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0

print(ans)

# Два цикла

ans = 0
for i in range(0, len(data) - 1):
    if data[i:i + 2] in 'AB AC':
        cnt = 1
        for j in range(i + 2, len(data) - 1, 2):
            if data[j:j + 2] in 'AB AC':
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
print()
