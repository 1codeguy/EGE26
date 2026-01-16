from itertools import product, permutations

def f(x, y, z, w):
    return (not (y <= (z == x))) and (w <= x)

for i in product((0, 1), repeat=7):
    table = [
        (i[0], 0, 0, i[1]),
        (0, i[2], 0, i[3]),
        (i[4], 1, i[5], i[6])
    ]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
                print(*p, sep='')