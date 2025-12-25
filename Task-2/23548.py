from itertools import product, permutations

def f(x, y, z, w):
    return ((x or y) <= z) or (y == w) or z

for i in product((0, 1), repeat=4):
    table = [
        (0, 1, i[0], i[1]),
        (1, i[2], 1, 0),
        (i[3], 1, 1, 0)
    ]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
                print(*p, sep='')