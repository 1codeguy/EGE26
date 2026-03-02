from re import finditer

with open(r'/Users/admin/Desktop/N24/24-371.txt') as file:
    data = file.readline()

patter = r'(A[^A.]*){98}\.'
matches = [match.group() for match in finditer(patter, data)]
print(len(min(matches, key=len)))