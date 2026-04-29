import joblib
import pandas as pd
from settings import settings
from logging_config import get_logger
from fastapi import FastAPI, HTTPException
from schemas import CreditInput, PredictionOutput

app = FastAPI()
logger = get_logger("api")

model = joblib.load(settings.model_path)
logger.info(f"Model loaded from {settings.model_path}")


@app.get("/")
def home():
    return {"message": "Credit Risk Model API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionOutput)
def predict(data: CreditInput):
    try:
        df = pd.DataFrame([data.model_dump()])
        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0][1]

        result = {
        "prediction": "Bad" if prediction == 1 else "Good",
        "risk_score": round(probability, 2)
        }

        logger.info(f"Prediction Made: {result}")
        return result

    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))