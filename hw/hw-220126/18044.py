from itertools import combinations

def f(x):
    M = 32 <= x <= 68
    N = 54 <= x <= 76
    A = A1 <= x <= A2
    return (not (M or N)) == (not A)

lineA = [32, 54, 68, 76]
lineX = [50, 60, 70]

ans = []
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans.append(A2 - A1)

print(min(ans))