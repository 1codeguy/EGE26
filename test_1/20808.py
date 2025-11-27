from string import printable as yoyo

def convert(num, sys):
    res = ''
    while num:
        res += yoyo[num % sys]
        num //= sys
    return res[::-1]

ans = 0
max_zero = 0
for x in range(1, 2031):
    num = convert(7**170 + 7**100 - x, 7)
    if num.count('0') >= max_zero:
        max_zero = num.count('0')
        ans = x
print(ans)