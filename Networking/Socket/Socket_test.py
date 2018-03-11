import socket

#SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(s)

server = 'www.google.com'

port = 80

#måte å få IP på

server_ip = socket.gethostbyname(server)

print(server_ip)

a = socket.getaddrinfo(server_ip, port = 80)

#print(a)

b = socket.gethostbyaddr(server_ip)

#print(b)


d = socket.gethostname()

print(d)
