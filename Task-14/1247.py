from string import printable

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

num = 729**8 - 3**18 + 85
num = convert(num, 9)
print(num.count('0'))