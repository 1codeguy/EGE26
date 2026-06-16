from ipaddress import *

def check(x):
    ip = f'{int(x):032b}'
    return ip.count('1') % 2 != 0

net = ip_network('172.16.128.0/255.255.192.0', False)

cnt = 0
for ip in net:
    if check(ip):
        cnt += 1

print(cnt)