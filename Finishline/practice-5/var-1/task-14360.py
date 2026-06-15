from ipaddress import ip_network, ip_address

ip_1 = '153.202.16.37'
network = ip_address('153.202.16.32')
for mask in range(10, 33):
    net = ip_network(f'{ip_1}/{mask}', False)
    if net.network_address == network:
        print(net.netmask)

print(255 + 248)