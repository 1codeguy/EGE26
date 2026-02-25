from re import finditer

with open(r'/Users/admin/Desktop/N24/24-320.txt') as file:
    data = file.readline()

num = r'([1-9][0-9]*|0)'
pattern = fr'({num}=)+{num}'
matches = [match.group() for match in finditer(pattern, data)]

ans = 0
for line in matches:
    new_line = line.split('=')
    for i in range(len(new_line) - 1):
        if new_line[i] == new_line[i + 1]:
            ans = max(ans, len(line))
            break
        elif len(new_line[i]) > len(new_line[i + 1]):
            changed_line = new_line[i]
            while changed_line and changed_line != new_line[i + 1]:
                changed_line = changed_line[1:]
            if changed_line == new_line[i + 1]:
                len_new_line = len(changed_line) + len('='.join(new_line[i + 1:])) + 1
                ans = max(ans, len_new_line)
        elif len(new_line[i]) < len(new_line[i + 1]):
            changed_line = new_line[i + 1]
            while changed_line and new_line[i] != changed_line:
                changed_line = changed_line[:-1]
            if new_line[i] == changed_line:
                len_new_line = len('='.join(new_line[:i + 1])) + len(changed_line) + 1
                ans = max(ans, len_new_line)

print(ans)
