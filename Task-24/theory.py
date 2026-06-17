from string import printable

N = 26
alph = printable.upper()[:N]
data = ''

# Все чётные числа в N чётной системе счисления
pattern = rf'[{alph[1:]}][{alph}]*[{alph[::2]}]'

# Все нечётные числа в N чётной системе счисления
pattern = rf'[{alph[1:]}][{alph}]*[{alph[1::2]}]'

#############################################
# В нечётной системе счисления не получится сразу определить чётность,
# поэтому сначала находим все числа из заданной системы,
# затем срезаем символы с конца/начала строки, пока не получим нужное число

pattern = rf'[{alph[1:]}][{alph}]*'
matches = []

ans = 0
for number in matches:
    len_number = len(number)
    if sum(map(lambda x: int(x, 36), number)) % 2 == 0:
        ans = max(ans, len_number)
    elif len_number > ans:
        for l in range(0, len_number):
            for r in range(len_number - 1, l, -1):
                new_number = number[l:r + 1]
                if sum(map(lambda x: int(x, 36), new_number)) % 2 == 0:
                    ans = max(ans, len(new_number))
                    break