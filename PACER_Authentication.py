import requests

# PACER Authentication API URL
# use auth_url_production if you are using the actual PACER production envirionment
#auth_url_production = "https://pacer.login.uscourts.gov/services/cso-auth"
auth_url = "https://qa-login.uscourts.gov/services/cso-auth"

# Replace with your PACER credentials
username = "enter your PACER username here"
password = "enter your PACER password here"
client_code = "optionalclientcode"  # Leave empty if not applicable
redact_flag = "1"  # Required for registered filers

# Prepare the request payload
payload = {
    "loginId": username,
    "password": password,
    "clientCode": client_code,  # Optional
    "redactFlag": redact_flag
}

# Prepare headers
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

try:
    # Send POST request to the authentication endpoint
    response = requests.post(auth_url, json=payload, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        response_data = response.json()
        if response_data["loginResult"] == "0":
            print("Authentication successful!")
            print("Authentication token:", response_data["nextGenCSO"])
        else:
            print("Authentication failed:", response_data.get("errorDescription", "Unknown error"))
    else:
        print(f"HTTP error occurred: {response.status_code} - {response.text}")
except Exception as e:
    print(f"An error occurred: {e}")
