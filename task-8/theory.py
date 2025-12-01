from itertools import *

# product - возвращает все возможные
# расстановки символов с повторениями длины repeat
alph_1 = 'ab'
for val in product(alph_1, repeat=2):
    val = ''.join(val)
    # print(val)

# permutations - возвращает все возможные перестановки символов
alph_2 = 'bb'
for val in permutations(alph_2):
    val = ''.join(val)
    print(val)

# enumerate
aplh_3 = 'melani'
res = enumerate(aplh_3, start=1)
print(*res)
