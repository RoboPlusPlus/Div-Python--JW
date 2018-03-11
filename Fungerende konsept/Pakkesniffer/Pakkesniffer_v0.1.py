import socket
import struct
import textwrap
##import os
##import sys
##import win32com.shell.shell as shell
##ASADMIN = 'asadmin'
##
##if sys.argv[-1] != ASADMIN:
##    script = os.path.abspath(sys.argv[0])
##    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
##    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
##    sys.exit(0)
    
#HOST = socket.gethostbyname(socket.gethostname())

def main():
    connection = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    host = socket.gethostbyname(socket.gethostname())
    print('IP: {}'.format(host))
    
    while True:
        raw_data, address = connection.recvfrom(65565) #65565
        destination_mac, source_mac, eth_proto, data = ethernet_frame_unpack(raw_data)
        print('\nEthernet Frame: ')
        print('Destination: {}, Source: {}, Protocol: {}'.format(destination_mac, source_mac, eth_proto))

# Unpacking av ethernet frame
    #6s = 6 byte
    #! = behandler som nettverksdata "little indian"
    #H = small unsigned int (tror jeg)
def ethernet_frame_unpack(data):
    destination_mac, source_mac, proto = struct.unpack('! 6S 6S H',data[:14]) #6+6+2 = 14
    return get_mac_addr(destination_mac), get_mac_addr(source_mac), socket.htons(proto), data[14:]

# Returnere menneske-lesbar MAC-adresse type 34:AB:34:...
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    mac_address = ':'.join(bytes_str).upper()
    return mac_address

main()
