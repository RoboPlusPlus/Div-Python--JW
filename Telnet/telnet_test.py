from telnetlib import Telnet

try:
    with Telnet("localhost", 23) as tn:
        tn.interact()
        print("Connected!")
except:
    print("could not connect to host")
