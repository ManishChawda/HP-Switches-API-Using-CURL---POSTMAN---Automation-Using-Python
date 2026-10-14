import requests
from credentials import ARUBA2530

switch_ip = ARUBA2530["host"]
username = ARUBA2530["username"]
password = ARUBA2530["password"]

session = requests.Session()

login_url = f"https://{switch_ip}/rest/v1/login-sessions"

login_response = session.post(
    login_url,
    json={
        "userName": username,
        "password": password
    },
    verify=False,
    timeout=10
)

print("Login Status:", login_response.status_code)
print("Login Response:", login_response.text)

# GET VLAN information
vlan_url = f"https://{switch_ip}/rest/v1/vlans"

vlan_response = session.get(
    vlan_url,
    verify=False,
    timeout=10
)

print("\nVLAN GET Status:", vlan_response.status_code)
print("VLAN Response:")
print(vlan_response.text)
