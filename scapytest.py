from scapy.all import *
import logging



b = Ether(src = "00:00:11:11:22:22")
c = b/IP("192.168.10.1")

print(repr(c))
