import io
import openpyxl
import pandas as pd
from fastapi import FastAPI
from data.data_source import get_businesses
from fastapi.responses import StreamingResponse



app = FastAPI()

@app.get("/")
def main():
    return {"message": "MVP Lead Gen API is working!"}

@app.get("/leads")
def get_leads(location: str, keyword: str, min_rating: float= 4.0, min_reviews: int= 50):
    return get_businesses(location, keyword, min_rating, min_reviews)

@app.get("/leads/excel")
def get_leads_excel(location: str, keyword: str, min_rating: float= 4.0, min_reviews: int= 50):
    data = get_businesses(location, keyword, min_rating, min_reviews)
    df = pd.DataFrame(data)

    stream = io.BytesIO()
    df.to_excel("leads.xlsx", index=False, engine="openpyxl")
    stream.seek(0)

    return StreamingResponse(
        stream,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=leads.xlsx"}
    )

