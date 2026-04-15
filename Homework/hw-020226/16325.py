from string import printable as pinkman

def convert(num, sys):
    res = ''
    while num:
        res += pinkman[num % sys]
        num //= sys
    return res[::-1]

num = convert(2*729**2014 + 2*243**2016 - \
              2*81**2018 + 2*27**2020 - 2*9**2022 - 2024, 27)

cnt = 0
for i in num:
    if int(i, 27) > 9:
        cnt += 1

print(cnt)