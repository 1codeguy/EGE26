from ipaddress import *

def check(x):
    ip = f'{int(x):032b}'
    return ip.count('1') % 5 == 0

net = ip_network('112.160.0.0/255.240.0.0', False)

cnt = 0
for ip in net:
    if check(ip):
        cnt += 1

print(cnt)