with open(r'files/26_15341.txt') as file:
    N = int(file.readline())
    pieces = [int(i) for i in file]

pieces = sorted(pieces, reverse=True)

cake = [pieces[0]]
for p in pieces[1:]:
    if p + 8 <= cake[-1]:
        cake.append(p)

print(len(cake), cake[-1])