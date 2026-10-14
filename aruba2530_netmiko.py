from credentials import ARUBA2530
from netmiko import ConnectHandler
import getpass

switch = {
    "device_type": ARUBA2530["device_type"],
    "host": ARUBA2530["host"],
    "port": ARUBA2530["port"],
    "username": ARUBA2530["username"],
    "password": ARUBA2530["password"],
}

connection = ConnectHandler(**switch)

print("Netmiko connection successful!")

connection.disconnect()

print("Netmiko connection closed.")
