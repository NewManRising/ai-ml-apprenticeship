# Imports
import pandas as pd
import matplotlib.pyplot as plt

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
# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Defining Column Types
num_cols = X.select_dtypes(include=["int64", "float64"]).columns
cat_cols = X.select_dtypes(include=["object", "str"]).columns

# Building Preprocessor
preprocessor = ColumnTransformer([
    ("num", StandardScaler(), num_cols),
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
])

# Building Pipeline
pipeline = Pipeline([
    ("preprocessing", preprocessor),
    ("model", RandomForestClassifier(random_state=42, class_weight="balanced", n_jobs=-1)),
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
# Extracting Model From Pipeline
best_pipeline = GS.best_estimator_
model = best_pipeline.named_steps["model"]

# Getting Feature Names
preprocessor = best_pipeline.named_steps["preprocessing"]
feature_names = preprocessor.get_feature_names_out()

importances = model.feature_importances_

# Creating DataFrame
feat_importance_df = pd.DataFrame({
    "feature": feature_names,
    "importance": importances
})

feat_importance_df.sort_values(by="importance", ascending=False, inplace=True)
print(feat_importance_df.head(10).to_string())
#----------------------------------------------------------------------------------------------------------------------
# Plotting Feature Importance
top_features = feat_importance_df.head(10)

plt.figure(figsize=(12, 8))
plt.barh(top_features["feature"], top_features["importance"])
plt.gca().invert_yaxis()

plt.title("Top Feature Importances")
plt.xlabel("Importance")

plt.tight_layout()

plt.savefig("feature_importance_plot.png")
plt.show()