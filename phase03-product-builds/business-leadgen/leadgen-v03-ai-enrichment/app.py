from fastapi import FastAPI
from data.google_places import search_google_places



app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Led Gen app is working!"}


@app.get("/leads")
def get_leads(location: str, keyword: str, min_rating: float = 4.0, min_reviews: int = 50):
    return search_google_places(location, keyword, min_rating, min_reviews)
