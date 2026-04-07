from itertools import combinations

def f(x):
    P = 5 <= x <= 280
    Q = 295 <= x <= 400
    R = 375 <= x <= 450
    A = A1 <= x <= A2
    return (Q <= P) or (not(A) <= R)

lineA = [5, 280, 295, 375, 400, 450]
lineX = [100, 290, 300, 380, 420]

ans = []
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans.append(A2 - A1)

print(min(ans))