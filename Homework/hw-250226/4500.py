from functools import lru_cache

@lru_cache(None)
def f(start, end, eleven=False, last=''):
    if start == 11: eleven = True
    if start > 11 and not eleven: return 0
    if start > end or start == 23: return 0
    if start == end and eleven: return 1
    if last == 'A':
        return f(start + 2, end, eleven, 'B') + \
            f(start * 2, end, eleven, 'C')
    return f(start + 1, end, eleven, 'A') + \
        f(start + 2, end, eleven, 'B') + \
        f(start * 2, end, eleven, 'C')

print(f(3, 79))