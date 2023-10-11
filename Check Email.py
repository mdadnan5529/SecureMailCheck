import requests

def check_email_breaches(email):
    # HIBP API endpoint for searching breaches by email
    api_url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"

    # Set up the request headers with your HIBP API key
    headers = {
        "User-Agent": "YourAppName",  # Replace with your app name
        "hibp-api-key": "YOUR_HIBP_API_KEY"  # Replace with your HIBP API key
    }

    try:
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            breaches = response.json()
            if not breaches:
                return f"The email address '{email}' has not been involved in any breaches."
            else:
                return f"The email address '{email}' has been involved in the following breaches:\n" + ", ".join(breaches)
        elif response.status_code == 404:
            return f"The email address '{email}' has not been found in any breaches."
        else:
            return "An error occurred while checking the email address."
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    email_to_check = input("Enter the email address to check: ")
    result = check_email_breaches(email_to_check)
    print(result)
