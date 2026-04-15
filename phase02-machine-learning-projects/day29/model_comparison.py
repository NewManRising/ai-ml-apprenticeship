# Imports
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
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
models = {
    "LogisticRegression": LogisticRegression(random_state=42, max_iter=1000, class_weight="balanced"),
    "RandomForest": RandomForestClassifier(random_state=42, class_weight="balanced", n_jobs=-1),
    "GradientBoosting": GradientBoostingClassifier()
}

results = []

for name, model in models.items():

    pipeline = Pipeline([
    ("preprocessing", preprocessor),
    ("model", model)
])

    pipeline.fit(X_train, y_train)
#----------------------------------------------------------------------------------------------------------------------
# Evaluation & Results
    y_pred = pipeline.predict(X_test)

    report = classification_report(y_test, y_pred, output_dict=True)

    results.append({
    "model": name,
    "precision_1": report["1"]["precision"],
    "recall_1": report["1"]["recall"],
    "f1_1": report["1"]["f1-score"],
    "accuracy": report["accuracy"],

})


    print(f"\n{name}")
    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))

    results_df = pd.DataFrame(results)
    print(results_df.sort_values(by="f1_1", ascending=False))