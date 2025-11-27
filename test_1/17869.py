from string import printable as dc

def convert(num, sys):
    res = ''
    while num:
        res += dc[num % sys]
        num //= sys
    return res[::-1]

num = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2025
num = convert(num, 25)
print(num.count('0'))