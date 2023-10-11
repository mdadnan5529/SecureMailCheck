import requests
import hashlib

def check_leaked_password(password):
    # Hash the password using SHA-1 (HIBP API requires the password to be hashed)
    password_hash = hashlib.sha1(password.encode()).hexdigest().upper()

    # Split the hash into the prefix and suffix
    prefix, suffix = password_hash[:5], password_hash[5:]

    # Make a GET request to the HIBP API
    api_url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(api_url)

    if response.status_code == 200:
        # Check if the password's hash suffix exists in the response
        hashes = response.text.splitlines()
        for line in hashes:
            if line.startswith(suffix):
                return f"The password '{password}' has been found in breaches {line.split(':')[1]} times."
        
        return f"The password '{password}' has not been found in any breaches."
    elif response.status_code == 404:
        return "HIBP API not found."
    else:
        return "An error occurred while checking the password."

if __name__ == "__main__":
    password_to_check = input("Enter the password to check: ")
    result = check_leaked_password(password_to_check)
    print(result)
