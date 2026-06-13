def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(1, 2031):
    num = convert(6**2030 + 6**100 - x, 6)
    ans.append(num.count('0'))

print(min(ans))