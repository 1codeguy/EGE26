from re import finditer
with open(r'/Users/admin/Desktop/N24/24_14510.txt') as file:
    data = file.readline()

vowels = r'[AEIOUY]'
consonants = '[^AEIOUY]'
group = rf'{consonants}{consonants}{vowels}'
pattern = rf'{group}(.*?{group}){{499}}'

matches = [match.group() for match in finditer(pattern, data)]
print(len(min(matches, key=len)))