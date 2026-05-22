import os
import requests
from dotenv import load_dotenv

load_dotenv()

PLACES_KEY = os.getenv("GOOGLE_PLACES_API_KEY")

def search_google_places(location, keyword):
    url = "https://places.googleapis.com/v1/places:searchText"


    headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": PLACES_KEY,
    "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.rating,places.userRatingCount,places.types,places.websiteUri,places.nationalPhoneNumber,places.businessStatus,places.id"
}


    params = {
    "textQuery": f"{keyword} in {location}",
    "pageSize": 5,
    "strictTypeFiltering": True
}

    response = requests.post(url, headers=headers, json=params)
    data = response.json()


    def cleaned_json(results):
        cleaned = []

        for place in results:
            business_url = place.get("websiteUri", "")
            clean_url = business_url.split("?")[0]

            business = {
                "name": place.get("displayName", {}).get("text", ""),
                "address": place.get("formattedAddress", ""),
                "phone": place.get("nationalPhoneNumber", ""),
                "website": clean_url,
                "rating": place.get("rating", ""),
                "reviews": place.get("userRatingCount", ""),
                "status": place.get("businessStatus", ""),

            }

            cleaned.append(business)

        return cleaned
    raw_results = data.get("places", [])

    cleaned_results = cleaned_json(raw_results)

    return cleaned_results

