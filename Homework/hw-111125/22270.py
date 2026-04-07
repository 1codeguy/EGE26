def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num = num // sys
    return res[::-1]

for n in range(1, 100_000):
    r = convert(n, 4)
    if int(r[:1]) == 3:
