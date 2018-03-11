from pysnmp.hlapi import UsmUserData
a = UsmUserData('testuser', authKey='authenticationkey')
AUTHKEY = "horse"
a.userName='testuser'
a.authKey= "horse"
a.privKey= ""
a.authProtocol=(1,3,6,1,6,3,10,1,1,2)
a.privProtocol=(1,3,6,1,6,3,10,1,2,1)
UsmUserData('testuser', authKey='authenticationkey', privKey='encryptionkey')
b = UsmUserData(userName='testuser', authKey="", privKey=<PRIVKEY>, authProtocol=(1,3,6,1,6,3,10,1,1,2), privProtocol=(1,3,6,1,6,3,10,1,2,2))
