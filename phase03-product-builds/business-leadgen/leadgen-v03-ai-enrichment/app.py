from fastapi import FastAPI, HTTPException
from data.google_places import search_google_places



app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Led Gen app is working!"}


@app.get("/leads")
def get_leads(location: str, keyword: str, min_rating: float = 4.0, min_reviews: int = 50, demo: bool = False):
    try:
        return search_google_places(location, keyword, min_rating, min_reviews, demo)
    except RuntimeError as e:
        raise HTTPException(status_code=502, detail=str(e))
