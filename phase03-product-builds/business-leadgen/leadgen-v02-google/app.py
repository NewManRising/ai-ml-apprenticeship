import io
import pandas as pd
from fastapi import FastAPI
from data.google_places import search_google_places
from fastapi.responses import StreamingResponse


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Google Led Gen app is working!"}


@app.get("/leads")
def get_leads(location: str, keyword: str, min_rating: float = 4.0, min_reviews: int = 50):
    return search_google_places(location, keyword, min_rating, min_reviews)



@app.get("/leads/excel")
def get_leads_excel(location: str, keyword: str, min_rating: float= 4.0, min_reviews: int= 50):
    data = search_google_places(location, keyword, min_rating, min_reviews)
    df = pd.DataFrame(data)

    stream = io.BytesIO()
    df.to_excel(stream, index=False, engine="openpyxl")
    stream.seek(0)

    return StreamingResponse(
        stream,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=leads.xlsx"}
    )

