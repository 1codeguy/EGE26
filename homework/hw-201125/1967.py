from string import printable

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

num = 3*4**38 + 2*4**23 + 4**20 + 3*4**5 + 2*4**4 + 1
num = convert(num, 16)
print(num.count('0'))

