from ipaddress import *

ip = ip_address('218.48.192.56')

cnt = 0
for mask in range(16, 25):
    net = ip_network(f'{ip}/{mask}', False)
    if net.network_address == ip_address('218.48.192.0') and net.num_addresses - 2 >= 500:
        cnt += 1

print(cnt)