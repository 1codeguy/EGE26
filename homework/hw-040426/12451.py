```
from ipaddress import ip_network

def f(ip):
    ip = f'{int(ip):032b}'
    return ip[16:25].count('0') > ip[25:].count('0')

cnt = 0
for A in range(0, 256):
    net = ip_network(f'246.81.65.{A}/255.255.255.224', False)
    hosts = list(net.hosts())
    if all(f(ip) for ip in hosts):
        cnt += 1

print(cnt)
```