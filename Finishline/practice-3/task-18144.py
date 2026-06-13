def f(x, s):
    if x <= 19: return s % 2 == 0
    if s == 0: return 0
    if x % 2 == 0:
        h = [f(x - 4, s - 1),
             f(x - 6, s - 1),
             f(x // 2, s - 1)]
    else:
        h = [f(x - 4, s - 1),
             f(x - 6, s - 1),
             f(x // 2 + 1, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('19)', min(i for i in range(20, 200) if f(i, 2)))
print('20)', [i for i in range(20, 200) if f(i, 3) and not f(i, 1)])
print('21)', max(i for i in range(20, 200) if f(i, 4) and not f(i, 2)))