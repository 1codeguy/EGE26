from string import printable as che

def convert(num, sys):
    res = ''
    while num:
        res += che[num % sys]
        num //= sys
    return res[::-1]

num = 15625**16 - 3125**3*25**19 + 625**4 - 2005
num = convert(num, 5)
print(num.count('0'))