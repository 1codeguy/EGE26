from itertools import permutations

graph = 'FA AC CE EG GF AB BF DC DH HE'.split()
matrix = '68 47 45 237 368 15 248 157'.split()

print(*range(1,9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
# 18