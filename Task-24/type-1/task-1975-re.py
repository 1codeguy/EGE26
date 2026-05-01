from re import finditer

with open(r'../files/24_1975.txt') as file:
    data = file.readline()

patter = r'(?=P)P([^P]+P?)+[^P]+P(?<=P)'
matches = [match.group() for match in finditer(patter, data)]
print(len(max(matches, key=len)))