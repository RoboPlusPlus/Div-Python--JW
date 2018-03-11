import socket
import struct
#import binascii
import textwrap
import urllib.request as urllib2
import json
import codecs
import time





def main():
    #Setup vars:
    max_packet_count = 20
    packet_count = 0
    all_mac_addresses = set()

    
    # Get host
    host = socket.gethostbyname(socket.gethostname())
    print('IP: {}'.format(host))

    # Create a raw socket and bind it
    conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    conn.bind((host, 0))

    # Include IP headers
    conn.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    # Enable promiscuous mode
    conn.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    

    while packet_count <= max_packet_count:
        # Recive data
        raw_data, addr = conn.recvfrom(65536)

        # Unpack data
        dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)

        print('\nEthernet Frame:')
        print("Destination MAC: {}".format(dest_mac))
        print("Source MAC: {}".format(src_mac))
        print("Protocol: {}".format(eth_proto))
        packet_count = packet_count +1
        all_mac_addresses.add(str(dest_mac))
        all_mac_addresses.add(str(src_mac))


    all_mac_addresses = sorted(all_mac_addresses)
    print ("\nAntallMAC-adresser: " + str(len(all_mac_addresses))+ "\nSortert:")


    print ("Content-Type: text/html\n")

    all_vendor_addresses = set()

    for mac_address in all_mac_addresses:
        all_vendor_addresses.add(mac_address[:9] + "00:00:00")

    for mac_address in sorted(all_vendor_addresses):
        print(mac_address)
        #API base url,you can also use https if you need
        url = "http://macvendors.co/api/"

        try:
            request = urllib2.Request(url+mac_address, headers={'User-Agent' : "API Browser"}) 
            response = urllib2.urlopen( request )
            #Fix: json object must be str, not 'bytes'
            reader = codecs.getreader("utf-8")
            obj = json.load(reader(response))

            #Print company name
            print (obj['result']['company']+"<br/>");

            #print company address
            print (obj['result']['address']);
        except:
            print("Cannot resolve vendor from MAC-address: " + mac_address)

        #time.sleep(1)
        




# Unpack ethernet frame
def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('!6s6s2s', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), get_protocol(proto), data[14:]

# Return formatted MAC address AA:BB:CC:DD:EE:FF
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    mac_address = ':'.join(bytes_str).upper()
    return mac_address

# Return formatted protocol ABCD
def get_protocol(bytes_proto):
    bytes_str = map('{:02x}'.format, bytes_proto)
    protocol = ''.join(bytes_str).upper()
    return protocol

#main()
