from re import finditer
from string import digits

digits = digits[::2]

with open(r'files/24_23206.txt') as file:
    data = file.readline()

pattern = fr'[02468][^S{digits}]*(S[^S{digits}]*){{35}}[^S{digits}]*'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))