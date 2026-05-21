from fastapi import FastAPI
from data.google_places import search_google_places


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Google Led Gen app working!"}


@app.get("/leads")
def get_leads(location: str, keyword: str):
    return search_google_places(location, keyword)