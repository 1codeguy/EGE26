from itertools import permutations

graph = 'BE EG GA AF FC CD DB BC GF'.split()
matrix = '24 134 267 125 47 37 356'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)