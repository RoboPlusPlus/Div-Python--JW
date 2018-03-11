import sys, paramiko


hostname = "test.rebex.net"
password = "password"
command = "ls /tmp/doc "

username = "demo"
port = 22

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.WarningPolicy)

client.set_missing_host_key_policy(paramiko.WarningPolicy())

client.connect(hostname, port=port, username=username, password=password)

stdin, stdout, stderr = client.exec_command(command)
print(stdout.read())


client.close()