def f(start, end, s=''):
    if start > end: return 0
    if start == end:
        if s.count('1') < 5 and s.count('2') >= 2 and s.count('3') == 5:
            return 1
        return 0
    return f(start * 5, end, s + '1') + f(start * 3, end, s + '2') + f(start + 45, end, s + '3')

print(f(1, 2970))