from string import digits
with (open(r'/Users/admin/Desktop/N24/24-293.txt') as file):
    data = file.readline()

# data = '***DSDS*D**DS**SD'

data = data.replace('DS', 'D S')
data = data.replace('SD', 'S D')
data = data.split()

max_len_line = 0

for line in data:
    s = [i for i in range(len(line)) if line[i] == 'D']

    for i in range(1, len(s) - 101):
        start = s[i - 1]
        end = s[i + 100] + 1
        full_line = line[start:end]
        if not any(j in digits for j in full_line):
            max_len_line = max(max_len_line, len(full_line) - 2)

print(max_len_line)

