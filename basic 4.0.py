import requests
import logging
import os
#import time
from requests.exceptions import RequestException, Timeout, TooManyRedirects, HTTPError, ConnectionError

# Configure logging
current_dir = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(current_dir, 'website_checker.log')

logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(asctime)s - %(levelname)s: %(message)s')

"""
def check_website_periodically(url, interval=60):
    while True:
        check_website(url)
        time.sleep(interval)

"""

def check_website(url, timeout=10):
    try:
        response = requests.get(url, timeout=timeout, allow_redirects=True)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        if 200 <= response.status_code < 300:
            logging.info(f"The website {url} is live and running fine!")
        else:
            logging.error(f"The website {url} returned status code: {response.status_code}")
    except Timeout:
        logging.error(f"Connection to {url} timed out after {timeout} seconds.")
    except TooManyRedirects:
        logging.error(f"Too many redirects while trying to connect to {url}.")
    except HTTPError as e:
        logging.error(f"HTTP error occurred while trying to connect to {url}: {e}")
    except ConnectionError as e:
        logging.error(f"Failed to establish a connection to {url}: {e}")
    except RequestException as e:
        logging.error(f"An error occurred while trying to connect to {url}: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Example usage
website_urls = [
    "https://www.google.com/",
    "https://www.youtube.com/"
]

for url in website_urls:
    logging.info(f"Checking website: {url}")
    check_website(url)