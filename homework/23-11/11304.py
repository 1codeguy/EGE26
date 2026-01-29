from string import printable as hell

for x in hell[:16]:
    num1 = int(f'11{x}73', 16)
    num2 = int(f'94662{x}53{x}', 16)
    num3 = int(f'6{x}41', 16)
    num4 = int(f'31{x}77', 16)
    num5 = int(f'9{x}82{x}{x}181', 16)
    num = num1 + num2 + num3 + num4 + num5
    if num % 15 == 0:
        print(num / 15)
