from credentials import ARUBA2530
import requests
import urllib3

urllib3.disable_warnings()

switch_ip = ARUBA2530["host"]
username = ARUBA2530["username"]
password = ARUBA2530["password"]

session = requests.Session()

# -------------------------
# LOGIN
# -------------------------

login_url = f"https://{switch_ip}/rest/v1/login-sessions"

login_response = session.post(
    login_url,
    json={
        "userName": username,
        "password": password
    },
    verify=False
)

print("Login Status:", login_response.status_code)
print("Login Response:", login_response.text)

# -------------------------
# STORE ARUBA SESSION COOKIE
# -------------------------

login_data = login_response.json()

aruba_cookie = login_data["cookie"]

cookie_name, cookie_value = aruba_cookie.split("=", 1)

session.cookies.set(
    cookie_name,
    cookie_value,
    domain=switch_ip,
    path="/"
)

print("Session cookie stored successfully.")

# -------------------------
# GET VLAN INFORMATION
# -------------------------

vlan_url = f"https://{switch_ip}/rest/v1/vlans"

vlan_response = session.get(
    vlan_url,
    verify=False
)

print("\nVLAN GET Status:", vlan_response.status_code)
print("VLAN Response:")
print(vlan_response.text)

# -------------------------
# LOGOUT
# -------------------------

logout_url = f"https://{switch_ip}/rest/v1/login-sessions"

logout_response = session.delete(
    logout_url,
    verify=False
)

print("\nLogout Status:", logout_response.status_code)
print("Logout Response:", logout_response.text)
