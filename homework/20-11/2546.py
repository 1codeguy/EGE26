from string import printable

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res

num = 4**36 + 3*4**20 + 4**15 + 2*4**7 + 49
num = convert(num, 16)
