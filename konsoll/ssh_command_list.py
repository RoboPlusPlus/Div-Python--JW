import paramiko, sys

def sshCommand(_hostname, _port, _username, _password, _command):
    sshClient = paramiko.SSHClient()

    sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshClient.load_system_host_keys()
    sshClient.connect(_hostname, _port, _username, _password)
    stdin, stdout, stderr =sshClient.exec_command(_command)
    try:
        print(stdout.read())
    except:
        print("no stdout\n")

    try:
        print(stderr.read())
    except:
        print("no stderr\n")
    try:
        print(stdin.read())
    except:
        print("no stdin\n")

    sshClient.close()

command_list = ["su", "__Dund3r__", "whoami", "apt-get update", "apt-get install python3"]

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("args missing")
        for entry in command_list:
            sshCommand('192.168.10.125', 22, 'pi', 'raspberry', entry)
        sys.exit(1)
    else:
        for entry in command_list:
            hostname = sys.argv[1]
            username = sys.argv[2]
            password = sys.argv[3]
            #command = sys.argv[4]
            sshCommand(hostname, 22, username, password, entry )


