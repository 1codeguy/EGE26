from ipaddress import ip_network, ip_address


ip_1 = r'121.171.5.70'
ip_2 = r'121.171.5.107'
for mask in range(10, 31):
    net = ip_network(f'{ip_1}/{mask}', False)
    if ip_address(ip_1) in net.hosts() and ip_address(ip_2) in net.hosts():
        print(net.num_addresses)