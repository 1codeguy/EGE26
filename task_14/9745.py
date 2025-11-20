from string import printable as code10


for x in code10[:19]:
    num1 = int(f'98{x}79641', 19)
    num2 = int(f'36{x}14', 19)
    num3 = int(f'73{x}4', 19)
    num = num1 + num2 + num3
    if num % 18 == 0:
        print(num // 18)




