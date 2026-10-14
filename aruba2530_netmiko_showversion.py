from netmiko import ConnectHandler
from credentials import ARUBA2530
import getpass

switch = {
    "host": ARUBA2530["host"],
    "port": ARUBA2530["port"],
    "device_type": ARUBA2530["device_type"],
    "username": ARUBA2530["username"],
    "password": ARUBA2530["password"],
}

connection = ConnectHandler(**switch)

print("Netmiko connection successful!")

output = connection.send_command("show version")

print(output)

connection.disconnect()
print("Netmiko connection closed.")
