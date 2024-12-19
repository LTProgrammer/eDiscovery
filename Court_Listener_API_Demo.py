import requests

def search_case(api_token, case_name):
    """
    Search for a case using the CourtListener API and print details for cases matching the exact name.

    Parameters:
        api_token (str): API token for authentication.
        case_name (str): The name of the case to search for.
    """
    # API endpoint
    url = "https://www.courtlistener.com/api/rest/v4/search/"

    # Query parameters
    params = {
        "q": f'"{case_name}"',  # Search query with exact phrase match
    }

    # Headers with authorization token
    headers = {
        "Authorization": f"Token {api_token}"
    }

    try:
        # Perform the API request
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return

    # Parse the JSON response
    data = response.json()

    # 'results' will contain the list of cases
    results = data.get('results', [])

    if results:
        print("\nSearch Results (Exact Name Match):")
        found_match = False
        for result in results:
            # Confirm exact match for caseName
            if result.get('caseName', '').strip() == case_name.strip():
                found_match = True
                case_title = result.get('caseName', 'Unknown Title')
                current_status = result.get('status', 'Unknown Status')
                date_filed = result.get('dateFiled', 'Unknown Date')
                court_name = result.get('court', 'Unknown Court')
                judge_name = result.get('judge', 'Unknown Judge')
                attorneys = result.get('attorney', 'Unknown Attorney(s)')

                # Print the case details
                print(f"- Case Title: {case_title}")
                print(f"  Current Status: {current_status}")
                print(f"  Date Filed: {date_filed}")
                print(f"  Court: {court_name}")
                print(f"  Judge: {judge_name}")
                print(f"  Attorney(s): {attorneys}")
                print()

        if not found_match:
            print("No cases found with the exact name provided.")
    else:
        print("\nNo cases found for the given name.")

# Main function
if __name__ == "__main__":
    # Prompt the user for API token
    api_token = input("Enter your API token: ").strip()

    # Prompt the user for case name
    case_name = input("Enter the exact name of the case: ").strip()

    # Call the function to search for the case
    search_case(api_token, case_name)
