import joblib
import pandas as pd
from fastapi import FastAPI
#----------------------------------------------------------------------------------------------------------------------
app = FastAPI()

model = joblib.load("models/best_credit_model.pkl")

@app.get("/")
def home():
    return {"message": "Credit Risk Model API is running"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return {
        "prediction": "Bad" if prediction == 1 else "Good",
        "risk_score": round(probability, 2)
    }