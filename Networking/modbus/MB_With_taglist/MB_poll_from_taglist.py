from pymodbus3.client.sync import ModbusTcpClient 
import time as t
from twisted.internet import reactor, protocol
from pymodbus3.constants import Defaults
import logging

#Setup
logging.basicConfig()
clientIP = '10.181.5.34'
clientPort = 502
TagFilePath = "Taglist.txt"


#Filehandler taglist
#Creating a list of all the tags imported from the file
with open(TagFilePath, 'r') as fhand:
    tagimport=[]
    for lines in fhand:
        tagimport.append(str(lines))   
    
class tag():
    def __init__(self, tagnumber, tagname, address, access):
        self._tagnumber = tagnumber
        self._tagname = tagname
        self._address = address
        self._access = access

def read_all(_taglist):
    a=1
    for i in _taglist:
        _tag = _taglist[a]
        _tagname, _address, _access, dataType = _tag
        if "r" in _access:
            rr = client.read_coils(_address,1)
            print(_tagname, rr)
        a+=1


# Placing all the tags in the tags dict
tags = [] #list for all the  imported tags
tl = str
i=0


for line in tagimport:
    tl  = tagimport[i]
    tl.rstrip()
    a = tl.split(',')
    name, address, access, dataType = a
    address = (address.zfill(5))
    dataType = dataType.rstrip()
    tags.append((name, address, access, dataType))
    i+=1

#tags[1].append(2)


#print(tags)

client = ModbusTcpClient(clientIP, port=clientPort)
go = 1
while go == 1:
    read_all(tags)
    go = 0












    
    
