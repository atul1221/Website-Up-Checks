import requests

def check_website(url):
    try:
        response = requests.get(url)
        # Check if the status code is in the range of 200 to 299
        if 200 <= response.status_code < 300:
            print(f"The website {url} is live and running fine!")
        else:
            print(f"The website {url} returned status code: {response.status_code}")
    except requests.ConnectionError:
        print(f"Failed to connect to {url}")

# Example usage
website_url = "https://www.google.com/"
check_website(website_url)

