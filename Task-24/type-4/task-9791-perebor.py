from string import ascii_uppercase, digits

with open(r'../files/24_9791.txt') as file:
    data = file.readline()

alph = digits + ascii_uppercase[:6]

ans = 0
for i in range(len(data) - 1):
    if data[i] in alph[1:] and data[i + 1] in alph:
        cnt = 2
        for j in range(i + 2, len(data)):
            if data[j] in alph:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 0
                break
print(ans)

