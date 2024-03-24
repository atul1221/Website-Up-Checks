import requests
from requests.exceptions import RequestException

def check_website(url, timeout=10):
    try:
        response = requests.get(url, timeout=timeout, allow_redirects=True)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        print(f"The website {url} is live and running fine!")
    except requests.Timeout:
        print(f"Connection to {url} timed out after {timeout} seconds.")
    except requests.TooManyRedirects:
        print(f"Too many redirects while trying to connect to {url}.")
    except requests.RequestException as e:
        print(f"An error occurred while trying to connect to {url}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
website_url = "https://www.google.com/"
check_website(website_url)
