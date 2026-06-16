from itertools import combinations


def f(x):
    P = 25 <= x <= 64
    Q = 40 <= x <= 115
    A = A1 <= x <= A2
    return P <= ((Q and not A) <= (not P))

lineA = [25, 40, 64, 115]
lineX = [30, 50, 100]

ans = []
for A1, A2 in combinations(lineA, r=2):
    if all(f(x) for x in lineX):
        ans.append(A2 - A1)

print(min(ans))