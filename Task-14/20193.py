from string import printable

ans = []
for x in printable[:18]:
    num1 = int(f'11h{x}05', 18)
    num2 = int(f'3f{x}54{x}8', 18)
    num3 = int(f'g{x}{x}{x}9', 18)
    num = num1 + num2 + num3
    if num % 14 == 0:
        print(num // 14)
        break
