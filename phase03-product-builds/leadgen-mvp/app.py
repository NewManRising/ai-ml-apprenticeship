from fastapi import FastAPI
from data.data_source import get_businesses

app = FastAPI()

@app.get("/")
def main():
    return {"message": "MVP Lead Gen API is working!"}

@app.get("/leads")
def get_leads(city: str, keyword: str):
    return get_businesses(city, keyword)

