from string import printable as ysl

for x in ysl[:26]:
    num1 = int(f'27{x}98876', 26)
    num2 = int(f'26{x}51', 26)
    num3 = int(f'15{x}47', 26)
    num4 = int(f'62{x}5', 26)
    num = num1 + num2 + num3 + num4
    if num % 25 == 0:
        print(num // 25)
        break