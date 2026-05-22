from re import *
with open(r'../files/24_16388.txt') as file:
    data = file.readline()

pattern = r'(LMN|MN|N)?(KLMN)+(KLM|KL|K)?'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

################################################

data = data.replace('KLMN', '****')
data = data.replace('LMN*', ' ****')
data = data.replace('MN*', ' ***')
data = data.replace('N*', ' **')
data = data.replace('*KLM', '**** ')
data = data.replace('*KL', '*** ')
data = data.replace('*K', '** ')

for i in 'KLMN':
    data = data.replace(i, ' ')

data = data.split()
print(len(max(data, key=len)))