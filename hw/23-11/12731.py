from string import printable as eboi

min_x = 100_000
for x in eboi[:14]:
    num1 = int(f'9{x}ab', 14)
    num2 = int(f'{x}46c', 14)
    num3 = int(f'b7{x}')
    num = num1 + num2 - num3
    if num % 13 == 0 and int(x, 14) < min_x:
        ans = num // 13

print(ans)