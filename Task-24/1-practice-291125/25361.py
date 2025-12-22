# from re import*

with open(r'../files/24_25361.txt') as file:
    data = file.readline()

for i in '02468':
    data = data.replace(i, ' 0')
data = data.split()

ans = []
for i in data:
    if i[0] == '0':
        if i.count('F') == 76:
            ans.append(len(i))
        elif i.count('F') > 76:
            while i.count('F') > 76:
                num = i.rfind('F')
                i = i[:num]
            ans.append(len(i))

print(max(ans))

##########################

# pattern = r'[02468]([^02468F]*F){76}[^02468F]*'
#
# matches = [match.group() for match in finditer(pattern,data)]
#
# print(len(max(matches, key=len)))