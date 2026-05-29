from itertools import permutations

graph = 'FE EG GB BA AH CB CG CD DF'.split()
matrix = '47 458 67 125 246 35 138 27'.split()

print(*range(1, 9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

print(38 + 19)