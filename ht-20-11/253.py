from string import printable

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

for i in range(2, 10):
    if convert(41, i) % i == 2 and convert(131, i) % i == 1:
        print(sys)