import ipaddress, netifaces
from ipaddress import IPv4Network
adr = ipaddress.ip_network('192.168.0.0/28')

print(adr)

for addr in IPv4Network('192.0.2.0/27'):
    print(addr)

#print(netifaces.interfaces())
print(netifaces.AF_LINK)



#print(netifaces.ifaddresses("150DC9A5-E6CB-40CE-A02F-749D68210EA2"))
