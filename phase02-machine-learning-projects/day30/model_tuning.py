# Imports
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import confusion_matrix, classification_report
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

forest = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestClassifier(random_state=42, class_weight="balanced", n_jobs=-1)),
])

# Setting Parameters
logreg_params = {
    "model__C": [0.01, 0.1, 1, 10],
    "model__solver": ["liblinear", "lbfgs"]
}

rf_params = {
    "model__n_estimators": [100, 200, 300],
    "model__max_depth": [None, 2, 5],
    "model__min_samples_leaf": [2, 3, 5]
}


# Creating GridSearchCV
log_regGS = GridSearchCV(
    log_reg,
    param_grid=logreg_params,
    cv=5,
    scoring="f1",
    n_jobs=-1,
)

forestGS = GridSearchCV(
    forest,
    param_grid=rf_params,
    cv=5,
    scoring="f1",
    n_jobs=-1,
)


# Training Models
log_regGS.fit(X_train, y_train)
forestGS.fit(X_train, y_train)
#----------------------------------------------------------------------------------------------------------------------
# Results & Evaluation
results = []

models = {
    "Tuned Logistic Regression": log_regGS,
    "Tuned Random Forest": forestGS,
}

for name, gs_model in models.items():
    y_pred = gs_model.best_estimator_.predict(X_test)
    report = classification_report(y_test, y_pred, output_dict=True)

    # noinspection PyTypeChecker
    results.append({
        "model": name,
        "best_params": gs_model.best_params_,
        "cv_best_f1": gs_model.best_score_,
        "precision_1": report["1"]["precision"],
        "recall_1": report["1"]["recall"],
        "f1_1": report["1"]["f1-score"],
        "accuracy": report["accuracy"]
    })

    print(f"\n{name}")
    print("Best Params:", gs_model.best_params_)
    print("Best CV F1-Score:", gs_model.best_score_)
    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))


# Comparison Table
results_df = pd.DataFrame(results)
print('\n*** Tuned Model Comparison ***\n')
print(results_df.sort_values(by="f1_1", ascending=False).to_string())