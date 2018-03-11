from opcua import Client

path = "opc.tcp://192.168.10.141:49320/OPCUA/Kepware.KEPServerEX.V5/"
client = Client(path)
#client.server_url = "POWERTOWER", path

client.connect()
print(client.get_namespace_array())
print("Server node = " + str(client.get_server_node()) + "\n")
objects = client.get_objects_node()
print("Objects: " + str(objects))
print("Children of objects are: ", objects.get_children())

var = objects.get_child(["3:Channel1.Device1", "tag1"])
print(var)
print("Value of variable is: ", str(var.get_value()))
print(client.get_node(2))

client.disconnect()
"""
Children of objects are:  [Node(FourByteNodeId(i=2253)), Node(StringNodeId(ns=2;s=_AdvancedTags)), 
Node(StringNodeId(ns=2;s=_CustomAlarms)), Node(StringNodeId(ns=2;s=_DataLogger)), Node(StringNodeId(ns=2;s=_OracleConnector)), 
Node(StringNodeId(ns=2;s=_Redundancy)), Node(StringNodeId(ns=2;s=_SNMP Agent)), Node(StringNodeId(ns=2;s=_System)), 
Node(StringNodeId(ns=2;s=Channel1))]

"""