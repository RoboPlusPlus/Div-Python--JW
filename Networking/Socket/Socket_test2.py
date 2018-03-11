import socket

#SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(s)

servers = ['www.google.com', 'www.vg.no', 'www.dn.no', 'www.aventi.no', 'www.hest.no']

port = 80

#måte å få IP på

for server in servers:
    server_ip = socket.gethostbyname(server)
    print(server + " " + server_ip)

    a = socket.getaddrinfo(server_ip, port = 80)

    #b = socket.gethostbyaddr(server_ip)

    #print(b)


    #d = socket.gethostname()

    #print(d)
