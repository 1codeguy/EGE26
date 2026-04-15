from itertools import product

alph1 = 'КОНЕЦ'
alph2 = 'ДРАКОН'
sp1 = []
sp2 = []

for val in product(alph1, repeat=5):
    val = ''.join(val)
    sp1.append(val)

for word in product(alph2, repeat=5):
    word = ''.join(word)
    sp2.append(word)

cnt = 0
for i in sp1:
    if i not in sp2:
        cnt += 1
for i in sp2:
    if i not in sp1:
        cnt += 1

print(cnt)