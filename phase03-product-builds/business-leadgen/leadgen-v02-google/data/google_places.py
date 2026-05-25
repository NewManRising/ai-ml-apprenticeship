import os
import requests
from dotenv import load_dotenv

load_dotenv()

PLACES_KEY = os.getenv("GOOGLE_PLACES_API_KEY")

def search_google_places(location, keyword, min_rating, min_reviews):
    url = "https://places.googleapis.com/v1/places:searchText"


    headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": PLACES_KEY,
    "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.rating,places.userRatingCount,places.websiteUri,places.nationalPhoneNumber,places.businessStatus,places.id"
}


    params = {
    "textQuery": f"{keyword} in {location}",
    "pageSize": 5,
    "minRating": min_rating,
    "openNow": True,
    "languageCode": "en-US",

}

    response = requests.post(url, headers=headers, json=params)
    response.raise_for_status()
    data = response.json()

    def cleaned_json(results):

        filtered = []

        for place in results:

            business_url = place.get("websiteUri", "")
            clean_url = business_url.split("?")[0]

            rating = place.get("rating", 0) or 0
            reviews = place.get("userRatingCount", 0) or 0
            status = place.get("businessStatus", "")

            if status != "OPERATIONAL":
                continue

            if rating < min_rating:
                continue

            if reviews < min_reviews:
                continue

            rating_score = (rating / 5) * 70
            review_score = (min(reviews, 500) / 500) * 30

            business = {
                "Name": place.get("displayName", {}).get("text", ""),
                "Address": place.get("formattedAddress", ""),
                "Phone": place.get("nationalPhoneNumber", ""),
                "Website": clean_url,
                "Rating": rating,
                "Reviews": reviews,
                "Status": status,
                "Score": round(rating_score + review_score, 2)
            }

            filtered.append(business)

        filtered.sort(key=lambda x: x["Score"], reverse=True)

        return filtered




    raw_results = data.get("places", [])

    cleaned_results = cleaned_json(raw_results)

    return cleaned_results

