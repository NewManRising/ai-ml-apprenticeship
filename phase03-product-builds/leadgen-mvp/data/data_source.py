import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YELP_API_KEY")

def get_businesses(city: str, keyword: str):
    url = "https://api.yelp.com/v3/businesses/search"

    headers = {"Authorization": f"Bearer {API_KEY}"
    }

    params = {
        "location": city,
        "term": keyword,
        "limit": 5
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    yelp_businesses = data.get("businesses", [])
    businesses_list = []
    

    for business in yelp_businesses:
        businesses_list.append({
            "name": business.get("name"),
            "rating": business.get("rating"),
            "reviews": business.get("review_count"),
            "address": ",".join(business.get("location", {}).get("display_address", [])),
            "phone": business.get("display_phone"),
            "out of business": business.get("is_closed"),
            "url": business.get("url")

        })
    return businesses_list



