from string import printable

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

num = 16**820 - 2**761 + 14
num = convert(num, 4)
print(num.count('0'))

