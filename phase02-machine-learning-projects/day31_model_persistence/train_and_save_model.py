# Imports
import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
#----------------------------------------------------------------------------------------------------------------------
# Loading Data
data = pd.read_csv("cleaned_credit_data.csv")
df = data.copy()

#----------------------------------------------------------------------------------------------------------------------
# Defining Features
X = df.drop(columns=["risk"])
y = df["risk"]

y = y.map({"good": 0, "bad": 1})
#----------------------------------------------------------------------------------------------------------------------
# Engineering New Features
X["credit_group"] = pd.qcut(X["credit_amount"], q=3, labels=["low", "medium", "high"])

X["purpose_credit_interaction"] = X["purpose"] + "_" + X["credit_group"].astype(str)

X["housing_savings"] = X["housing"] + "_" + X["saving_accounts"]
#----------------------------------------------------------------------------------------------------------------------
# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y )

# Defining Column Data Types To A Variable
num_cols = X.select_dtypes(include=["number", "int64", "float64"]).columns
cat_cols = X.select_dtypes(include=["object", "category", "str"]).columns
#----------------------------------------------------------------------------------------------------------------------
# Building Preprocessor
preprocessor = ColumnTransformer([
    ("num", StandardScaler(), num_cols),
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
])

# Creating Pipeline For Each Model
log_reg = Pipeline([
    ("preprocessor", preprocessor),
    ("model", LogisticRegression(random_state=42, max_iter=1000, class_weight="balanced")),
])


# Setting Parameters
logreg_params = {
    "model__C": [0.01, 0.1, 1, 10],
    "model__solver": ["liblinear", "lbfgs"]
}


# Creating GridSearchCV
log_regGS = GridSearchCV(
    log_reg,
    param_grid=logreg_params,
    cv=5,
    scoring="f1",
    n_jobs=-1,
)

# Training Models
log_regGS.fit(X_train, y_train)
#----------------------------------------------------------------------------------------------------------------------
# Saving Model
best_model = log_regGS.best_estimator_
joblib.dump(best_model, "models/best_credit_model.pkl")


