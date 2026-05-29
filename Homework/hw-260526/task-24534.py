def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(1, 11_501):
    num = 7**270 + 7**170 + 7**70 - x
    ans.append([convert(num, 7).count('0'), x])

print(max(ans))
