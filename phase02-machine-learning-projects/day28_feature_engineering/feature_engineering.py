# Imports
import pandas as pd

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
#----------------------------------------------------------------------------------------------------------------------
# Loading Data
data = pd.read_csv("cleaned_credit_data.csv")
df = data.copy()

# Quick Look At Data
print(df.head(5).to_string())
#----------------------------------------------------------------------------------------------------------------------
# Defining Features
X = df.drop(columns=["risk"])
y = df["risk"]

y = y.map({"good": 0, "bad": 1})

print("\nFeatures Shape:", X.shape)
print("Labels Shape:", y.shape)
print("Target Distribution:\n", y.value_counts())
#----------------------------------------------------------------------------------------------------------------------
# Engineering New Features
X["credit_group"] = pd.qcut(X["credit_amount"], q=3, labels=["low", "medium", "high"])

X["purpose_credit_interaction"] = X["purpose"] + "_" + X["credit_group"].astype(str)

X["housing_savings"] = X["housing"] + "_" + X["saving_accounts"]
#----------------------------------------------------------------------------------------------------------------------
# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Defining Column Types
num_cols = X.select_dtypes(include=["int64", "float64"]).columns
cat_cols = X.select_dtypes(include=["object", "str", "category"]).columns

# Building Preprocessor
preprocessor = ColumnTransformer([
    ("num", StandardScaler(), num_cols),
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
])

# Building Pipeline
pipeline = Pipeline([
    ("preprocessing", preprocessor),
    ("model", RandomForestClassifier(random_state=42, class_weight="balanced", n_jobs=-1))
])
#----------------------------------------------------------------------------------------------------------------------
# GridSearchCV Parameters
params = {
    "model__n_estimators": [100, 200, 300],
    "model__max_depth": [None, 2, 5],
    "model__min_samples_leaf": [2, 3, 5]
}

# Fitting Model
GS = GridSearchCV(pipeline, param_grid=params, cv=5, scoring="f1")
GS.fit(X_train, y_train)
#----------------------------------------------------------------------------------------------------------------------
# Evaluation & Results
y_pred = GS.best_estimator_.predict(X_test)

print("\n** Results **\n")
print("Classification Report: \n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))