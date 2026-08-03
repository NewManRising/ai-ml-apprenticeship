import requests
from bs4 import BeautifulSoup



def extract_website_text(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

    except requests.RequestException:
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    # Removes HTML tags
    for tag in soup(["script", "style", "noscript", "header", "footer", "nav"]):
        tag.decompose()

    text = soup.get_text(strip=True)

    # Collapse repeated spaces, tabs, and newlines
    text = " ".join(text.split())

    # Limit text to 5000 characters before sending it to an LLM
    text = text[:5000]

    return text
    

print(extract_website_text("https://www.gametz.com"))

