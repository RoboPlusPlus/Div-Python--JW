
from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command
import threading

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that some hosts may not respond to a ping request even if the host name is valid.
    """

    # Ping parameters as function of OS
    parameters = "-n 1" if system_name().lower()=="windows" else "-c 1"

    # Pinging
    return system_call("ping " + parameters + " " + host) == 0

def pingEdit(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that some hosts may not respond to a ping request even if the host name is valid.
    """

    # Ping parameters as function of OS
    parameters = "-n 1" if system_name().lower()=="windows" else "-c 1"

    # Pinging
    pingSuccess = (system_call("ping " + parameters + " " + host) == 0)
    #return pingSuccess, parameters, host


pingList = ['216.58.211.132']

threads = []
for node in pingList:
    t = threading.Thread(target=pingEdit(node))
    threads.append(t)
    t.start()

    #a = pingEdit(node)
    #print(type(a))
    #print(a)


