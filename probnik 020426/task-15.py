from itertools import product

def f(x):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = A1 <= x <= A2
    return P <= ((Q and not(A)) <= (not(P)))

lineA = [15, 21, 40, 63]
lineX = [20, 30, 50]

ans = []
for A1, A2 in product(lineA, repeat=2):
    if all(f(x) for x in lineX):
        ans.append(A2 - A1)

print(min(ans))