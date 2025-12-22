from itertools import permutations

graph = 'КГ ГВ ВА АБ БВ ВД ДЕ ЕК ГЕ ВЕ АВ'.split()
matrix = '24 146 56 1267 36 23457 46'.split()

print(*range(1,8))
for i in permutations('АБВГДЕК'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
# 30