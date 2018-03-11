import subprocess

hosts_file = open("hosts.txt","r")
lines = hosts_file.readlines()

for line in lines:
    line = line.strip()
    ping = subprocess.Popen(["ping", "-n", "3",line],stdout = subprocess.PIPE,stderr = subprocess.PIPE,shell =True)
    out, error = ping.communicate()
    out = out.strip()
    error = error.strip()
    output = open("PingResults.txt",'a')
    output.write(str(out))
    output.write(str(error))
    print(out.decode('utf-8'))
    print(error.decode('utf-8'))
hosts_file.close()
