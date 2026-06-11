with open(r'files/26_17643.txt') as file:
    N = int(file.readline())
    goods = []
    for i in file:
        goods += [list(map(int, i.split())) for i in file]

moda = 0

max(for good in goods)