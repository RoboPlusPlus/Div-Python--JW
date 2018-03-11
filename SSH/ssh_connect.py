import paramiko
host = "test.rebex.net" #"192.168.10.165"

ssh = paramiko.SSHClient()

ssh.load_system_host_keys()

#Dersom det ikke finnes noen policy, så setter en automatisk
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print(ssh)
ssh.connect(host, port=22, username="demo", password="password")
print("ssh connected")
stdin, stdout, stderr = ssh.exec_command("show ip interface brief")
output = stdout.readlines()
type(output)
print(type(stdout))
print(stdout)
for line in stdout:
    print("..." + line.strip("\n"))
ssh.close()
