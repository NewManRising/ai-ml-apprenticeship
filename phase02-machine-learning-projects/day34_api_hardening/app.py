import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from schemas import CreditInput, PredictionOutput

app = FastAPI()
model = joblib.load("models/best_credit_model.pkl")

@app.get("/")
def home():
    return {"message": "Credit Risk Model API is running"}

@app.post("/predict", response_model=PredictionOutput)
def predict(data: CreditInput):
    try:
        df = pd.DataFrame([data.model_dump()])
        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0][1]

        return {
        "prediction": "Bad" if prediction == 1 else "Good",
        "risk_score": round(probability, 2)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))