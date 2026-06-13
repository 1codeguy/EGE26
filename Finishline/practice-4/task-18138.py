from ipaddress import ip_network

def f(ip):
    ip = f'{int(ip):032b}'
    return ip.count('0') % 7 == 0

for mask in range(24, 33):
    net = ip_network(f'172.16.168.0/{mask}')
    if sum(1 for i in net if f(i)) == 35:
        print(net.netmask)