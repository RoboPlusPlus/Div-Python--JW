from pymodbus3.client.sync import ModbusTcpClient #.client.sync
import time as t
from twisted.internet import reactor, protocol
from pymodbus3.constants import Defaults

import logging
logging.basicConfig()
a=1
client = ModbusTcpClient('10.181.5.35', port=502)

rq = client.write_coil(1, True)
rr = client.read_coils(1,1)
assert(rq.function_code < 0x80)     # test that we are not an error
assert(rr.bits[0] == True)          # test the expected value
#result = client.read_coils(0,1)
"""arguments = {
    'read_address':    1,
    'read_count':      8,
    'write_address':   1,
    'write_registers': [20]*8,"""

while a<4:
    rq = client.write_registers(0, [0]*15)
    rq2 = client.write_registers(1000, [241]*100) #Startadresse, skrevet verdi, antall registre
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    client.write_coil(0, True)
    client.write_coil(1, True)
    client.write_coil(2, False)
    client.write_coil(3, True)
    #t.sleep(0.5)
    
    result = client.read_coils(0,1000)
    result2 = client.read_coils(1000,1000)
    #rr = client.read_input_registers(1,8)
    print (result.bits[0])
    print (result.bits[1])
    print (result.bits[2])
    print (result.bits[3])
    #print (result.bits[30])
    #print (result.bits[50])
    #client.close()
    lengthArr = len(result.bits)    
    print(lengthArr)
    t.sleep(0.5)
    a=a+1
"""
f= open("MBreads.txt", 'r+')
s= str
c = len(result.bits)
for i in range (0, c):
    s= ("Address {0} has value {1}\n".format(i, result.bits[i]))
    f.write(s)
    f.close()
"""


client.close()
