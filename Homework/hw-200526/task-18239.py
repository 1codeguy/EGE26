from functools import lru_cache
from re import finditer

@lru_cache(None)
def eval(match):
    return eval(match) > -20_000

with open(r'/Users/admin/Desktop/N24/24_18239.txt') as file:
    data = file.readline()

num = r'[1-9][1-9]*'
pattern = fr'({num}-)*{num}'

matches = [match.group() for match in finditer(pattern, data)]


ans = max(len(match) for match in matches if eval(match))

print(ans)