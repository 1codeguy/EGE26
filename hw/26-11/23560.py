def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


for x in range(1, 2401):
    num_10 = 7*9**210 + 6*9**110 - x
    num_9 = convert(num_10, 9)
    if num_9.count('0') == 100:
        print(x)