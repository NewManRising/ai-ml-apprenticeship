import os
import requests
from dotenv import load_dotenv
from ai.company_enrichment import summarize_company
from ai.website_extractor import extract_website_text


load_dotenv()

PLACES_KEY = os.getenv("GOOGLE_PLACES_API_KEY")
if not PLACES_KEY:
    raise RuntimeError("Please set GOOGLE_PLACES_API_KEY environment variable")

def search_google_places(location, keyword, min_rating, min_reviews, demo: bool = False):
    if demo:
        return [
            {
                "Name": "Summit Roofing & Exteriors",
                "Address": "1420 Oakwood Dr, Fort Worth, TX",
                "Phone": "(817) 555-0142",
                "Website": "https://summitroofingtx.com",
                "Rating": 4.8,
                "Reviews": 312,
                "Status": "OPERATIONAL",
                "Score": 85.72,
                "Company_Summary": "A family-owned residential and commercial roofing contractor serving the DFW area for over 15 years, specializing in storm damage repair and full roof replacement.",
                "Products_Services": ["Roof replacement", "Storm damage repair", "Gutter installation",
                                      "Free inspections"],
                "Sales_Insight": "Company emphasizes insurance claim assistance, suggesting they work with a high volume of storm-damage customers and may value tools that speed up lead qualification.",
                "Qualification": "HIGH",
                "Qualification_Reason": "Established local business with strong review volume and a service model well-suited to CRM or lead-tracking software."
            },
            {
                "Name": "Lone Star Pest Control",
                "Address": "889 Meadow Ln, Arlington, TX",
                "Phone": "(682) 555-0198",
                "Website": "https://lonestarpestcontrol.com",
                "Rating": 4.5,
                "Reviews": 176,
                "Status": "OPERATIONAL",
                "Score": 73.56,
                "Company_Summary": "A regional pest control provider offering residential and light commercial extermination and prevention plans.",
                "Products_Services": ["Pest inspection", "Quarterly treatment plans", "Termite control",
                                      "Rodent removal"],
                "Sales_Insight": "Recurring subscription-style service model indicates ongoing customer relationships that could benefit from automated scheduling or follow-up tools.",
                "Qualification": "MEDIUM",
                "Qualification_Reason": "Solid local presence, but website gives limited detail on current tech stack or pain points."
            },
            {
                "Name": "Prime Cut Landscaping",
                "Address": "204 Birchwood Ct, Grapevine, TX",
                "Phone": "(214) 555-0173",
                "Website": "https://primecutlandscapingtx.com",
                "Rating": 4.2,
                "Reviews": 64,
                "Status": "OPERATIONAL",
                "Score": 62.64,
                "Company_Summary": "A small landscaping and lawn care company serving residential clients in the northern DFW suburbs.",
                "Products_Services": ["Lawn maintenance", "Landscape design", "Irrigation repair"],
                "Sales_Insight": "Small team size and limited review volume suggest a business still scaling operations — may be receptive to affordable automation tools.",
                "Qualification": "MEDIUM",
                "Qualification_Reason": "Smaller operation with room to grow; fit depends on budget more than need."
            },
            {
                "Name": "Direct Path Logistics",
                "Address": "3350 Commerce Pkwy, Irving, TX",
                "Phone": "(972) 555-0110",
                "Website": "https://directpathlogistics.com",
                "Rating": 4.9,
                "Reviews": 421,
                "Status": "OPERATIONAL",
                "Score": 96.86,
                "Company_Summary": "A mid-sized freight and logistics company coordinating regional trucking and warehousing services across North Texas.",
                "Products_Services": ["Freight brokerage", "Warehousing", "Last-mile delivery", "Fleet management"],
                "Sales_Insight": "High review volume and established operations suggest a sizable customer base — a strong candidate for higher-value B2B software or automation contracts.",
                "Qualification": "HIGH",
                "Qualification_Reason": "Large, established operation with clear scale — likely already using or actively evaluating operational software."
            },
            {
                "Name": "Ace Appliance Repair",
                "Address": "77 Sycamore St, Mansfield, TX",
                "Phone": "(817) 555-0199",
                "Website": "https://aceappliancerepairtx.com",
                "Rating": 4.1,
                "Reviews": 58,
                "Status": "OPERATIONAL",
                "Score": 60.28,
                "Company_Summary": None,
                "Products_Services": None,
                "Sales_Insight": None,
                "Qualification": None,
                "Qualification_Reason": None
            }
        ]

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
    "languageCode": "en-US",

}
    try:
        response = requests.post(url, headers=headers, json=params)
        response.raise_for_status()

        data = response.json()

    except requests.RequestException as e:
        raise RuntimeError(f"Google Places request failed: {e}")



    def cleaned_json(results):

        filtered = []

        for place in results:

            business_url = place.get("websiteUri", "")
            clean_url = business_url.split("?")[0]

            rating = place.get("rating", 0) or 0
            reviews = place.get("userRatingCount", 0) or 0
            status = place.get("businessStatus", "")

            # Filtering leads
            if status != "OPERATIONAL":
                continue

            if rating < min_rating:
                continue

            if reviews < min_reviews:
                continue

            # Scoring leads
            rating_score = (rating / 5) * 70
            review_score = (min(reviews, 500) / 500) * 30

            website_text = None
            ai_enrichment = None

            # Grabs cleaned website text
            if clean_url:
                website_text = extract_website_text(clean_url)

            # AI enrichment of text
            if website_text:
                try:
                    ai_enrichment = summarize_company(website_text)
                except Exception as e:
                    print(f"AI enrichment failed for {clean_url}: {e}")
                    ai_enrichment = None


            business = {
                "Name": place.get("displayName", {}).get("text", ""),
                "Address": place.get("formattedAddress", ""),
                "Phone": place.get("nationalPhoneNumber", ""),
                "Website": clean_url,
                "Rating": rating,
                "Reviews": reviews,
                "Status": status,
                "Score": round(rating_score + review_score, 2),
                "Company_Summary": ai_enrichment.company_summary if ai_enrichment else None,
                "Products_Services": ai_enrichment.products_services if ai_enrichment else None,
                "Sales_Insight": ai_enrichment.sales_insight if ai_enrichment else None,
                "Qualification": ai_enrichment.qualification.value if ai_enrichment else None,
                "Qualification_Reason": ai_enrichment.qualification_reason if ai_enrichment else None
            }

            filtered.append(business)

        filtered.sort(key=lambda x: x["Score"], reverse=True)

        return filtered




    raw_results = data.get("places", [])
    cleaned_results = cleaned_json(raw_results)

    return cleaned_results

