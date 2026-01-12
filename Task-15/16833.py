from itertools import combinations

def f(x):
    P = 25 <= x <= 73
    Q = 75 <= x <= 118
    A = A1 <= x <= A2
    return (A and (not Q)) <= (P or Q)

lineA = [25, 73, 75, 118]
linex = [50, 74, 100]

ans = []
for A1, A2 in combinations(lineA, r=2):
    if all(f(x) for x in linex):
        ans.append(A2 - A1)

print(max(ans))