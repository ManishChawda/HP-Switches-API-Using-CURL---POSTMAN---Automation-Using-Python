from credentials import ARUBA2530
import paramiko
import getpass
import time

switch_ip = ARUBA2530["host"]
ssh_port = ARUBA2530["port"]
username = ARUBA2530["username"]
password = ARUBA2530["password"]

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(
    hostname=switch_ip,
    port=ssh_port,
    username=username,
    password=password,
    look_for_keys=False,
    allow_agent=False,
    timeout=10
)

print("SSH connection successful!")


shell = ssh.invoke_shell()
time.sleep(2)

# Read initial banner and prompt
while shell.recv_ready():
    print(repr(shell.recv(65535).decode("utf-8", errors="replace")))

# Send the command
shell.sendall(b"\n")
time.sleep(1)

shell.sendall(b"show version\n")
time.sleep(3)

while shell.recv_ready():
    output = shell.recv(65535).decode("utf-8", errors="replace")
    print(output)

ssh.close()
print("SSH connection closed.")
