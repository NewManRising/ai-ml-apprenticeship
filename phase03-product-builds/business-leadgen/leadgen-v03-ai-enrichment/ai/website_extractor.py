import requests
from bs4 import BeautifulSoup



def extract_website_text(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()


    except requests.RequestException:

        return None

    soup = BeautifulSoup(response.text, "html.parser")

    # Removes HTML tags
    for tag in soup(["script", "style", "noscript", "header", "footer", "nav"]):
        tag.decompose()

    text = soup.get_text(separator=" ", strip=True)

    # Collapse repeated spaces, tabs, and newlines
    text = " ".join(text.split())

    # Prevents the LLM from extracting empty or useless text
    if len(text) < 100:

        return None

    # Limit text to 5000 characters before sending it to an LLM
    text = text[:5000]


    return text
    
