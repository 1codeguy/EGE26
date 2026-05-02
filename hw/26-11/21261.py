from dataclasses import replace
from string import printable

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

for n in range(1, 100_000):
    r = convert(n, 4)
    if sum(map(int, r)) % 3 == 0:
        k = replace
        print(k)


