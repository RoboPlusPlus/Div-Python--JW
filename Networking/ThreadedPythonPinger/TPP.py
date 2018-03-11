
from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command
import threading, time, pprint, os.path, subprocess
from time import localtime, strftime
print(strftime("%a, %d %b %Y %H:%M:%S,",localtime()))    #'Thu, 28 Jun 2001 14:17:15'

pingList = []
descriptions = []


address_list_filepath = "pinglist.txt"
ping_status = {}
old_ping_status = {}
lock = threading.Lock()
pingList_load_error = False


def load_ping_list(_load_filepath =  "pinglist.txt"):
    """
    Funksjonen tar argument som er filepath for fil som skal lastes
    Filen skal være kommaseparert med adresse til venstre, og beskrivelse
    til høyre.

    Funksjonen returnerer:
    list(adresser fra liste), list(beskrivelse fra liste), bool(load_error)

    
    """
    _load_error = False
    _addresses = []
    _descriptions = []
    _data = []
    if not os.path.isfile(_load_filepath):


        try:
            f = open(_load_filepath,'w')
            f.close()
        except OSError as err:
            print("OS error: {0}".format(err))
            _load_error = True
        except:
            print("Unexpected error:", sys.exc_info()[0])
            _load_error = True
            raise
            
    if os.path.isfile(_load_filepath):
        try:
            with open(_load_filepath,'r') as f:
                _data = f.readlines()
             
            for line in _data:
                words = line.split(",")
                _address, *_description = words
                _addresses.append(_address)
                _descriptions.append(_description)
        except OSError as err:
            print("OS error: {0}".format(err))
            _load_error = True
        except ValueError:
            print("ValueError loading {}".format("pinglist.txt"))
            _load_error = True
        except:
            print("Unexpected error:", sys.exc_info()[0])
            _load_error = True
            raise
    return _addresses, _descriptions, _load_error

def pinger(host):

    # Finner om system er windows eller Linux
    parameters = "-n 1" if system_name().lower()=="windows" else "-c 1"

    # Pinger, og returnerer tuple.
    return (system_call("ping " + parameters + " " + host) == 0, parameters, host)

def pinger2(host):
    #line = line.strip()
    ping = subprocess.Popen(["ping", "-n", "3",host],stdout = subprocess.PIPE,stderr = subprocess.PIPE,shell =True)
    out, error = ping.communicate()
    out = out.strip()
    error = error.strip()
    #output = open("PingResults.txt",'a')
    #output.write(str(out))
    #output.write(str(error))
    print(out.decode('utf-8'))
    print(error.decode('utf-8'))
    #hosts_file.close()
    return True, True, host

    
def initiate(_pingList):
    for node in _pingList:
        ping_status.update({node: False})
        t = threading.Thread(target=ping_handler(node))
        t.daemon = True

def cycle(_pingList):
    for node in _pingList:
        t = threading.Thread(target=ping_handler(node))
        t.daemon = True
        t.start()


def ping_handler (node):
    _success, _parameters,  _host = pinger2(node)
    while lock.locked():
        time.sleep(0.01)
    lock.acquire()
    ping_status.update({_host: _success})
    lock.release()




file_load = load_ping_list(address_list_filepath)
pingList, descriptions, pingList_load_error = file_load
print(pingList)

initiate(pingList)
print("Active threads after initiate: " + str(threading.active_count()))
while True:
    
    print("Active threads in while loop: " + str(threading.active_count()))
    if old_ping_status == ping_status:
        #print('in IF old_ping_status == ping_status:')
        cycle(pingList)
    else:
        print('in ELSE old_ping_status == ping_status:')
        print(ping_status)
        old_ping_status = ping_status
        with open('pinglog_file.txt', 'a') as fh:
            Log_timestamp = strftime("\n\n%a, %d %b %Y %H:%M:%S\n",localtime())
            fh.write(Log_timestamp)
            fh.write("*"*len(Log_timestamp) + '\n')
            for node in pingList:
                print(ping_status.get(node))
                up_down_tag = "Up" if ping_status.get(node) == True else "Down"
                fh.write('{}: link {}\n'.format(node, up_down_tag))








