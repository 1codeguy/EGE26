# Псевдослучайные числа
from random import *

# randint() - генерирует одно число на заданном диапазоне.
# Возвращает int
rnd1 = randint(1,100)
print(rnd1)

# random() - генерирует одно число от 0 до 1.
# Возвращает float.
rnd2 = random()
print(rnd2)

# choice() - выбирает один случайный элемент из последовательности.
rnd3 = choice([0,7, 'hello', 7.4])
print(rnd3)

# sample() - выбирает k случайных элементов из последовательности.
rnd4 = sample([0,7, 'hello', 7.4], 3)
print(rnd4)