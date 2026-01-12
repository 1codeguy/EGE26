from itertools import permutations

graph = 'GF FD DB BA AC CE EG DE BC'.split()
matrix = '67 567 347 35 234 12 123'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)