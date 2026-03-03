from itertools import combinations

def f(x):
    B = 24 <= x <= 90
    C = 47 <= x <= 115
    A = A1 <= x <= A2
    return (C <= (not(A) and B)) <= (not(C))

lineA = [24, 47, 90, 115]
lineX = [30, 50, 100]

ans = []
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans.append(A2 - A1)

print(min(ans))