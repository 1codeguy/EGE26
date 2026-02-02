from itertools import permutations

graph = 'ЖЗ ЗА АБ БД ДЕ ЕЖ ЗЕ ГД ГВ ВБ ВА'.split()
matrix = '345 35 128 156 124 478 68 367'.split()

print(*range(1, 9))
for i in permutations('АБВГДЕЖЗ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
