def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = 0
cnt_4 = 0
for x in range(10, 70001):
    num = 5**2025 + 5**400 - x
    num = convert(num, 5)
    if num.count('4') >= cnt_4:
        cnt_4 = num.count('4')
        ans = x
print(ans)