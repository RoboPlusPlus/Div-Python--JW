import os, subprocess
"""
Legg til try, except osv


"""


def pinger2(_host, _number_of_pings = "3"):
    _ping_success = False
    _replies = []
    
    _ping_statistics ={
        "Packets_sent" : -1,
        "Received" : -1,
        "Lost": -1,
        "Round trip Minimum": -1,
        "Round trip Maximum": -1,
        "Round trip Average": -1,
        "Error": ""
        }

    _ping = subprocess.Popen(["tracert", "-n"],stdout = subprocess.PIPE,stderr = subprocess.PIPE,shell =False)
    out, error = _ping.communicate()
    out = out.strip()
    error = error.strip()
    _ping_statistics["Error"] = error.decode('utf-8')


    #Analyserer bytestring med ping-resultat
    _ping_result = out.decode('utf-8')
    _ping_result_lines = _ping_result.split("\n")

    for line in _ping_result_lines:
        if line.startswith("Reply from "):
            _replies.append(line)
        if line.startswith("    Packets: Sent = "):
            _fragmented_line = line.split(" ")
            _ping_statistics["Packets_sent"] = _fragmented_line[7].replace(",","")
            _ping_statistics["Received"] = _fragmented_line[10].replace(",","")
            _ping_statistics["Lost"] = _fragmented_line[13]
        
        if line.startswith("    Minimum = "):
            _fragmented_roundtrip_line = line.split(" ")
            _ping_statistics["Round trip Minimum"] = _fragmented_roundtrip_line[6].replace("ms","")
            _ping_statistics["Round trip Maximum"] = _fragmented_roundtrip_line[9].replace("ms","")
            _ping_statistics["Round trip Average"] = _fragmented_roundtrip_line[12].replace("ms","")

        if int(_ping_statistics["Received"]) >= 1 :
            _ping_success = True
            
    return _ping_success, _ping_statistics, _host

ping_success, ping_statistics, host = pinger2('216.58.209.100', "5")

print(ping_success)
print(ping_statistics)
print(host)


