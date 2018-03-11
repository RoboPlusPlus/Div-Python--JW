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
