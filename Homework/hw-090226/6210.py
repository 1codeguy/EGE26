from fnmatch import fnmatch

def f(num):
    d = set()
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}

    if len(d) > 30:
        return sum(d)
    return 0

for N in range(202 - 202 % 53, 10 ** 7 + 1, 53):
    if fnmatch(str(N), '*2?2*'):
        if str(N) == str(N)[::-1]:
            if F := f(N):
                print(N, F)
