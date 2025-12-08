from string import printable

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

max_x = 0
cnt = 0
for x in range(1, 10_001):
    num = 7**270 + 7**170 + 7**70 - x
    num = convert(num, 7)
    if num.count('0') >= cnt and x > max_x:
        cnt = num.count('0')
        max_x = x

print(max_x)

