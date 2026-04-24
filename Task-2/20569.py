from itertools import product, permutations

def f(x, y, w, z):
    return ((w <= z) == (x <= (not(y)))) and (x or z)

for i in product((0, 1), repeat=2):
    table = [
        (1, 0, 0, 1),
        (1, 1, 1, 0),
        (0, i[0], 0, i[1])
    ]
    if len(set(table)) == len(table):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, t))) for t in table] == [1, 0, 1]:
                print(*p)