from string import printable

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

num = 283**382 + 9**15 + 2**3
num = convert(num, 14)
print(num.count('b') - num.count('c'))

print(printable)
