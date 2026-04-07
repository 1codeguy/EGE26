from string import printable as skinhead

def convert(num, sys):
    res = ''
    while num:
        res += skinhead[num % sys]
        num //= sys
    return res[::-1]

for x in range(2005)[::-1]:
    num = 4**163*5 + 12**62 - x
    num = convert(num, 5)
    if num.count('1') < num.count('4'):
        print(x)
        break

