from itertools import product, permutations

def f(x, y, z, w):
    return not ((not (z <= y)) or (x == w) or x)

for i in product((0, 1), repeat=7):
    table = [
        (0, 0, i[0], i[1]),
        (i[2], i[3], 1, i[4]),
        (i[5], 1, 0, i[6])
        ]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
                print(*p, sep='')