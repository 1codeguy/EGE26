from ipaddress import ip_address, ip_network

ip_1 = '216.54.187.235'
ip_2 = '216.54.174.128'

for mask in range(10, 31):
    net_1 = ip_network(f'{ip_1}/{mask}', False)
    net_2 = ip_network(f'{ip_2}/{mask}', False)
    if ip_address(ip_1) in net_1.hosts() and ip_address(ip_1) not in net_2 and ip_address(ip_2) in net_2.hosts() and ip_address(ip_2) not in net_1:
        print(mask)