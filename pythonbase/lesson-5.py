# Работа с библиотеками

# Подключение библиотеки
import random
print(random.randint(1,100))

# Подключение библиотеки через псевдоним
import random as r
print(r.randint(1,100))

# Подключение одной команды из библиотеки
from random import randint
print(randint(1,100))

# Подключение одной команды из библиотеки
from random import randint
print(randint(1,100))

# Подключение одной команды из библиотеки через псевдоним
from random import randint as ri
print(ri(1,100))

# Подключение двух команд из библиотеки
from random import randint, choice
print(randint(1,100), choice([7, 5, 2, 0, 8]))

# Подключение двух команд из библиотеки через псевдоним
from random import randint as riri, choice as ch
print(riri(1,100), ch([7, 5, 2, 0, 8]))

# Подключение всех команд из библиотеки
from random import *
print(randint(1,100), choice([7, 5, 2, 0, 8]))