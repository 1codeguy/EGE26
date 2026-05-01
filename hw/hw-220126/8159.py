from itertools import combinations

def f(x):
    B = range(50, 71)
    for x in range(100):
        for y in range(100):
             F = (2*x + y != 150) or (x not in B) or (A > y)
             if not F:
                 return False
    return True

for A in range(100):
    if f(A):
        print(A)