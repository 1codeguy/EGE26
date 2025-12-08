def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(1, 3001):
    cnt = str(convert(4 ** 210 + 4 ** 110 - x, 4)).count('0')
    if cnt == 105:
        ans.append(x)

print(ans)