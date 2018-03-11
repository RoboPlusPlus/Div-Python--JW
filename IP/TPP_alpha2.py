"""
Todo

Pinger2 funksjon må oppdateres. Den er cowboy, men tror konseptet er bedre enn pinger1.



"""


import threading, time, pprint, os.path, subprocess, sys
from time import localtime, strftime
print(strftime("%a, %d %b %Y %H:%M:%S,",localtime()))    #'Thu, 28 Jun 2001 14:17:15'



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
            print("ValueError loading {}".format(_load_filepath))
            _load_error = True
        except:
            print("Unexpected error:", sys.exc_info()[0])
            _load_error = True
            raise
        if not _load_error:
            print("PingList loaded from {}_".format(_load_filepath))
    return _addresses, _descriptions, _load_error



import subprocess




def pinger(_host, _number_of_pings="1"):
    """
    :param _host: IP or Hostname
    :param _number_of_pings: Number of pings before returning
    :return: _ping_answer_from_host(bool), _ping_statistics(dict), _host(string)

    """

    _ping_answer_from_host = False
    _replies = []

    _ping_statistics = {
        "Packets_sent": -1,
        "Received": -1,
        "Lost": -1,
        "Round trip Minimum": -1,
        "Round trip Maximum": -1,
        "Round trip Average": -1,
        "Error": ""
    }

    try:
        _ping = subprocess.Popen(["ping", "-n", _number_of_pings, _host], stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, shell=True)
        out, error = _ping.communicate()
        out = out.strip()
        error = error.strip()
        _ping_statistics["Error"] = error.decode('utf-8')
        subprocess_success = True
    except:
        _ping_statistics["Error"] = "Could not successfully run subprocess"
        raise Exception("Could not successfully run subprocess")

    if subprocess_success:
        # Analyserer bytestring med ping-resultat
        _ping_result = out.decode('utf-8')
        _ping_result_lines = _ping_result.split("\n")

        for line in _ping_result_lines:
            if line.startswith("Reply from "):
                _replies.append(line)

            if line.find("Destination host unreachable."):
                _replies.append(line)

            if line.startswith("    Packets: Sent = "):
                _fragmented_line = line.split(" ")
                _ping_statistics["Packets_sent"] = _fragmented_line[7].replace(",", "")
                _ping_statistics["Received"] = _fragmented_line[10].replace(",", "")
                _ping_statistics["Lost"] = _fragmented_line[13]

            if line.startswith("    Minimum = "):
                _fragmented_roundtrip_line = line.split(" ")
                _ping_statistics["Round trip Minimum"] = _fragmented_roundtrip_line[6].replace("ms", "").replace(",", "")
                _ping_statistics["Round trip Maximum"] = _fragmented_roundtrip_line[9].replace("ms", "")
                _ping_statistics["Round trip Average"] = _fragmented_roundtrip_line[12].replace("ms", "")

            if int(_ping_statistics["Round trip Minimum"]) >= 0:
                _ping_answer_from_host = True

    return _ping_answer_from_host, _ping_statistics, _host

    
def initiate_ping_status(_pingList):
    _ping_status = {}
    for node in _pingList:
        _ping_status.update({node: False})
    return _ping_status


def start_threads(_pingList):
    _thread_number = 0
    for node in _pingList:
        _thread_number += 1
        t = threading.Thread(target= ping_handler, args = (node, _thread_number))
        t.daemon = True
        threads.append(t)

    for thread in threads:
        thread.start()

def ping_handler(node, _thread_number):
    _success, _ping_statistics, _host = pinger(node)
    access_pingstatus_lock.acquire()
    ping_status[_host] = _success
    access_pingstatus_lock.release()
    ping_statistics[node] = _ping_statistics


def continue_threads(_pingList):
    for i in range(len(threads)):
        pass
        #print(i)
        #if not threads[i] .isAlive:
         #   threads[i] = threading.Thread(target= ping_handler, args = (pingList[i], i))
          #  threads[i].daemon = True
           # threads[i].start()
            #print("Started new thread nr{} in continue_threads function".format(i))

    if threading.active_count() == 1:
        threads.clear()
        start_threads(_pingList)


access_pingstatus_lock = threading.Lock()
threads = []
address_list_filepath = "pinglist.txt"
file_load = load_ping_list(address_list_filepath)
pingList, descriptions, pingList_load_error = file_load
ping_status = initiate_ping_status(pingList)
ping_statistics = {}

def run():
    old_ping_status = {}
    print(ping_status)
    print("Active threads after initiate: " + str(threading.active_count()))
    start_threads(pingList)

    while True:
        print(ping_status)
        print(ping_statistics)
        continue_threads(pingList)
        time.sleep(2)
        print("Active threads in while loop: " + str(threading.active_count()))
        if old_ping_status != ping_status:
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



# run()


_xsuccess, _xping_statistics, _xhost = pinger("10.181.5.2")
print(_xsuccess)
print(_xping_statistics)
print(_xhost)



