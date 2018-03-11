from opcua import Client

path = "opc.tcp://192.168.10.141:49320/OPCUA/server/" # bare endre IP. Sjekk "OPC UA Configuration TAB i kepware(taskbar) og aktiver URL. Port skal være riktig
client = Client(path)

client.connect()
print(client.get_namespace_array())
print("Server node = " + str(client.get_server_node()) + "\n")
objects = client.get_objects_node()
print("Objects: " + str(objects))
for o in objects.get_children():
    print("Children of objects are: ", o)


root = client.get_root_node()
print("Root node is: ", root)
print("childs of root are: ", root.get_children())
print("name of root is", root.get_browse_name())

var = objects.get_child(["3:Channel1.Device1", "tag1"])
print(var)
print("Value of variable is: ", str(var.get_value()))

def get_children_names(_children):
    for i in _children:
        _val = str(i)
        int(_val.index("="))
        _index = [pos for pos, char in enumerate(_val) if char == "="]
        _index.reverse()
        _outval = _val[_index[0]+1: len(_val)]
        print(_outval)



get_children_names(objects.get_children())

print("getnode 1 :" + str(client.get_node(1)))

client.disconnect()