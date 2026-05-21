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
    "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.rating,places.userRatingCount,places.websiteUri,places.nationalPhoneNumber,places.id"
}


    params = {
    "textQuery": f"{keyword} in {location}",
    "pageSize": 5
}

    response = requests.post(url, headers=headers, json=params)
    data = response.json()
    print(data)
    return data