"""
SNMPv2c
+++++++

Send SNMP GET request using the following options:

* with SNMPv2c, community 'public'
* over IPv4/UDP
* to an Agent at demo.snmplabs.com:161
* for two OIDs in string form 

Functionally similar to:

| $ snmpget -v2c -c public demo.snmplabs.com 1.3.6.1.2.1.1.1.0 1.3.6.1.2.1.1.6.0

"""#
from pysnmp.hlapi import *

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData('public'),
           UdpTransportTarget(('192.168.10.125', 161)),
           ContextData(),
           ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0')),
           ObjectType(ObjectIdentity('1.3.6.1.2.27.4.0')),
           ObjectType(ObjectIdentity('1.3.6.1.2.1.1.2.0')),
           ObjectType(ObjectIdentity('1.3.6.1.2.1.1.2.1')),
           ObjectType(ObjectIdentity('1.3.6.1.2.1.1.6.0')),
           ObjectType(ObjectIdentity('1.3.6.1.2.1.1.4')),
           ObjectType(ObjectIdentity('1.3.6.1.2.1.1.6.0')),

           )
)


"""
1.3.6.1.1 - Directory
1.3.6.1.2 - Management (mgmt) <- Denne
1.3.6.1.3 - Experimental
1.3.6.1.4 - Private
1.3.6.1.5 - Security
1.3.6.1.6 - SNMPv2
1.3.6.1.7 - mail

1.3.6.1.2.27.4
1.3.6.1.2.1.1.2

1.3.6.1.2.1.1.1 - sysDescr
1.3.6.1.2.1.1.2 - sysObjectID
1.3.6.1.2.1.1.3 - sysUpTime
1.3.6.1.2.1.1.4 - sysContact
1.3.6.1.2.1.1.5 - sysName
1.3.6.1.2.1.1.6 - sysLocation
1.3.6.1.2.1.1.7 - sysServices
"""

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))
