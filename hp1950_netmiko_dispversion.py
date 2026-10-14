from netmiko import ConnectHandler
from credentials import HP1950
import getpass

switch = {
    "device_type": "hp_comware",
    "host": HP1950["host"],
    "port": HP1950["port"],
    "username": HP1950["username"],
    "password": HP1950["password"],
}

connection = ConnectHandler(**switch)

print("\nNetmiko SSH connection successful!")
print("Prompt:", connection.find_prompt())

# Enter extended CLI mode
print("\nEntering extended CLI mode...")

output = connection.send_command_timing("xtd-cli-mode")
print(output)

# Confirm extended CLI mode
output = connection.send_command_timing("Y")
print(output)

# Send extended CLI password
output = connection.send_command_timing(
    HP1950["extended_cli_password"],
    strip_prompt=False,
    strip_command=False
)
print(output)

# Check whether extended CLI authentication succeeded
if "Incorrect password" in output:
    print("Extended CLI authentication failed. Check the password.")
    connection.disconnect()
    raise SystemExit(1)

print("Extended CLI authentication response received.")

# Test command
output = connection.send_command_timing("display version")
print("\n--- DISPLAY VERSION ---")
print(output)

connection.disconnect()
print("\nConnection closed.")
