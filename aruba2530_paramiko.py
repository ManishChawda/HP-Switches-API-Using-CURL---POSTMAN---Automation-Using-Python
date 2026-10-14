from credentials import ARUBA2530
import paramiko
import getpass

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

ssh.close()
print("SSH connection closed.")
