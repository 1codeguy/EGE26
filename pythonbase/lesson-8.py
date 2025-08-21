# Циклы

# while - работает, пока выполняется условие
# num = 10
# while num >= 5:
#     print(num)
#     num -= 1

# continue - оператор перехода цикла на следующий шаг
# num = 10
# while num >= 5:
#     num -= 1
#     if num % 2 == 0:
#         continue
#     print(num)

# break - оператор прекращения работы цикла
# from random import randint
# while True:
#     num = randint(0, 100)
#     if num % 2 != 0:
#         print(num)
#         break
#     print(num)

# else - выполняет блок кода, если цикл завершится без break
# from random import randint
# num = 2
# while num >= 0:
#     rand_int = randint(0, 100)
#     if rand_int % 2 == 0:
#         break
#     print(rand_int)
#     num -= 1
# else:
#     print('все числа нечетные')

# Считать с клавиатуры число любой длины.
# Вывести на экран все цифры числа при помощи цикла While
# num = int(input())
# while num: # пока число существует или не превратилось в 0
#     print(num % 10)
#     num //= 10


# Цикл for - выполняет n-ое количество шагов
# for i in <итерируемый объект или последовательность>
# data = 'Hello'
# for i in data:
#     print(i)


# range(start, stop, step) - генерирует диапазон чисел от start до stop не включительно с шагом step

# for i in range(2):
#     print('hi', i)

# for i in range(5, 8): # -> 5, 6, 7
#     print('hi', i)

# for i in range(10, 5, -1): # -> 10, 9, 8, 7, 6
#     print('hi', i)

for i in range(187, 184, -1):
    print('hi', i)

