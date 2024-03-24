import requests
from requests.exceptions import RequestException, Timeout, TooManyRedirects, HTTPError, ConnectionError

def check_website(url, timeout=10):
    try:
        response = requests.get(url, timeout=timeout, allow_redirects=True)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        if 200 <= response.status_code < 300:
            print(f"The website {url} is live and running fine!")
        else:
            print(f"The website {url} is reachable but returned status code: {response.status_code}")
    except Timeout:
        print(f"Connection to {url} timed out after {timeout} seconds.")
    except TooManyRedirects:
        print(f"Too many redirects while trying to connect to {url}.")
    except HTTPError as e:
        print(f"HTTP error occurred while trying to connect to {url}: {e}")
    except ConnectionError as e:
        print(f"Failed to establish a connection to {url}: {e}")
    except RequestException as e:
        print(f"An error occurred while trying to connect to {url}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
website_urls = [
    "https://www.google.com/",
    "https://www.youtube.com/"
]

for url in website_urls:
    print(f"Checking website: {url}")
    check_website(url)
    print()
