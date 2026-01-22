from string import printable as juice
from math import log2

for x in juice[1:8]:
    num1 = int(f'{x}1{x}', 16)
    num2 = int(f'{x}3{x}3', 8)
    num = num1 + num2
    if log2(num) == int(log2(num)) and str(log2(num))[-1] == '0':
        print(x)

