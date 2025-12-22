def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for x in range(1, 2301):
    num = convert(7**350 + 7**150 - x, 7)
    if num.count('0') == 200:
        print(x)