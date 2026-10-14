from netmiko import ConnectHandler
from credentials import HP1950
import getpass

switch = {
    "device_type": HP1950["device_type"],
    "host": HP1950["host"],
    "port": HP1950["port"],
    "username": HP1950["username"],
    "password": HP1950["password"],
}

connection = ConnectHandler(**switch)

print("Netmiko SSH connection successful!")
print("Prompt:", connection.find_prompt())

connection.disconnect()
print("Connection closed.")
