from credentials import ARUBA2530
import requests

switch_ip = ARUBA2530["host"]
username = ARUBA2530["username"]
password = ARUBA2530["password"]

url = f"https://{switch_ip}/rest/v1/login-sessions"

response = requests.post(
    url,
    json={
        "userName": username,
        "password": password
    },
    verify=False
)

print("Status:", response.status_code)
print("Response:", response.text)
