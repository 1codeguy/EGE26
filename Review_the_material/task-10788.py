from ipaddress import ip_network, ip_address

ip_1 = '201.44.240.33'
ip_2 = '201.44.240.107'

cnt = 0
for mask in range(6, 32):
    net = ip_network(f'{ip_1}/{mask}', False)
    if ip_address(ip_1) in net.hosts() and ip_address(ip_2) in net.hosts():
        cnt += 1

print(cnt)