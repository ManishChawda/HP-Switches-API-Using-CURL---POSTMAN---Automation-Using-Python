from netmiko import ConnectHandler
from credentials import HPE5510
import getpass

switch = {
    "device_type": HPE5510["device_type"],
    "host": HPE5510["host"],
    "port": HPE5510["port"],
    "username": HPE5510["username"],
    "password": HPE5510["password"],
}

connection = ConnectHandler(**switch)

print("Netmiko connection successful!")

output = connection.send_command("display version")

print(output)

connection.disconnect()

print("Netmiko connection closed.")
