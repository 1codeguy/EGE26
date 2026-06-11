def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for x in range(2401):
    num = convert(7 * 9**210 + 6 * 9**110 - x, 9)
    if num.count('0') == 100:
        print(x)
