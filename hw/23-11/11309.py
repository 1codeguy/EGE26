from string import printable as p


min_x = 100_000
for x in p[:27]:
    num1 = int(f'8{x}38{x}68', 27)
    num2 = int(f'37{x}3163', 27)
    num = num1 + num2
    if num % 26 == 0 and int(x, 27) < min_x:
        ans = num // 26

print(ans)