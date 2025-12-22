print('x y z w')
for x in range(2):
    for y in 0, 1:
        for z in (0, 1):
            for w in [0, 1]:
                f = not (w <= x) or (x <= y) or not x
                if not f:
                    print(x, y, z, w)