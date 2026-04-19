# Imports
import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
#----------------------------------------------------------------------------------------------------------------------
# Loading Model
model = joblib.load("models/best_credit_model.pkl")


# Creating New Data To Pass To The Loaded Model
new_data = pd.DataFrame([{
    "age": 37,
    "sex": "male",
    "job": 2,
"housing": "own",
    "saving_accounts": "little",
    "checking_account": "moderate",
    "credit_amount": 3200,
    "duration": 18,
    "purpose": "car",
    "credit_group": "medium",
    "purpose_credit_interaction": "car_medium",
    "housing_savings": "own_little"
}])
#----------------------------------------------------------------------------------------------------------------------
# Making Prediction
prediction = model.predict(new_data)
probability = model.predict_proba(new_data)


print(f"Prediction: {"Good" if prediction[0] == 0 else "Bad"}")
print(f"Risk Score (Bad): {probability[0][1]:.2f}")