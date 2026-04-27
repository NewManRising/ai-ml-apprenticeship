from pydantic import BaseModel

class CreditInput(BaseModel):
    age: str
    sex: str
    job: int
    housing: str
    saving_accounts: str
    checking_account: str
    credit_amount: float
    duration: int
    purpose: str

class PredictionOutput(BaseModel):
    prediction: str
    risk_score: float