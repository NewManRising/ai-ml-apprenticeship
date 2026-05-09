import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YELP_API_KEY")

def get_businesses(location: str, keyword: str, min_rating=4.0, min_reviews=50):
    url = "https://api.yelp.com/v3/businesses/search"

    headers = {"Authorization": f"Bearer {API_KEY}"
    }

    params = {
        "location": location,
        "term": keyword,
        "limit": 5,
        "min_rating": min_rating,
        "min_reviews": min_reviews,
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    yelp_businesses = data.get("businesses", [])
    businesses_list = []
    

    for business in yelp_businesses:
        businesses_list.append({
            "Name": business.get("name"),
            "Rating": business.get("rating"),
            "Reviews": business.get("review_count"),
            "Address": ",".join(business.get("location", {}).get("display_address", [])),
            "Phone": business.get("display_phone"),
            "Out Of Business": business.get("is_closed"),
            "Url": business.get("url")

        })



    filtered = []

    for bus in businesses_list:
        if bus["Out Of Business"]:
            continue
        if bus["Rating"] < min_rating:
            continue
        if bus["Reviews"] < min_reviews:
            continue

        filtered.append(bus)

    for biz in filtered:
        score = (biz["Rating"] / 5 * 70) + (min(biz["Reviews"], 500) / 500 * 30)
        biz["Score"] = round(score, 2)

    filtered.sort(key=lambda x: x["Score"], reverse=True)


    return filtered


