from string import printable as dc

def convert(num, sys):
    res = ''
    while num:
        res += dc[num % sys]
        num //= sys
    return res[::-1]

for x in dc[:25]:
    num1 = int(f'A4{x}7f2', 25)
    num2 = int(f'n{x}g5{x}h', 25)
    num3 = int(f'74{x}m26', 25)
    num = num1 + num2 + num3
    if num % 24 == 0:
        print(num // 24)