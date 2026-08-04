from bs4 import BeautifulSoup
import requests

url = "https://www.whitehouse.gov/briefing-statements/"

def get_web_text(url):
    try:
        result = requests.get(url, timeout=10)
        result.raise_for_status()

    except requests.RequestException:
        return None

    soup = BeautifulSoup(result.text, "html.parser")