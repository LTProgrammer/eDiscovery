import requests

# PACER PCL API URLs
party_search_url = "https://qa-pcl.uscourts.gov/pcl-public-api/rest/parties/find"

# Replace with your authentication token
auth_token = "{replace your token here}"

# Request headers
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-NEXT-GEN-CSO": auth_token
}

# Request body
payload = {
    "lastName": "Henderson",
    "firstName": "Nicholas"
}

try:
    # Send POST request to perform the party search
    response = requests.post(party_search_url, json=payload, headers=headers)
    if response.status_code == 200:
        # Parse the response
        data = response.json()
        cases = data.get("content", [])
        
        # Print case titles
        print("Case Titles:")
        for case in cases:
            case_title = case.get("courtCase", {}).get("caseTitle", "No Title Found")
            print(case_title)
    else:
        print(f"Error: {response.status_code} - {response.text}")
except Exception as e:
    print(f"An error occurred: {e}")
