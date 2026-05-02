from string import printable

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

for x in range(1, 3001):
    num1 = int(convert(9*11**210, 11), 11)
    num2 = int(convert(8*11**150, 11), 11)
    num3 = int(convert(x, 11), 11)
    num = num1 + num2 - num3
    if str(num).count('0') == 60:
        print(x)
