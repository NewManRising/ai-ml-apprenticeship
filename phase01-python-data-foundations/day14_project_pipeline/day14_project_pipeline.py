# Imports
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

#----------------------------------------------------------------------------------------------------------------------

# Loading Data
data = pd.read_csv("day14_cleaned_data.csv")
df = data.copy()

# Inspecting the data
print("Shape of data:")
print(df.shape)

print("\nDataset Data Types:")
print(df.dtypes)

print("First Few Rows:")
print(df.head(3))

#----------------------------------------------------------------------------------------------------------------------

# Engineering Features
df["start_date"] = pd.to_datetime(df["start_date"])
df["start_month"] = df["start_date"].dt.month
df["start_year"] = df["start_date"].dt.year

# Creating Target Column
df["high_earner"] = df["salary"]  > 60000

# Saving Modified Dataset
df.to_csv("day14_cleaned_data.csv", index=False)
#----------------------------------------------------------------------------------------------------------------------

# Defining Features
X = df.drop(columns=["salary", "high_earner", "name", "start_date"])
y = df["high_earner"]

X = pd.get_dummies(X, columns=["department"], drop_first=True)

print("Feature Table Shape:\n", X.shape)
print("Feature Columns:\n", X.columns.tolist())
#----------------------------------------------------------------------------------------------------------------------

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print('Shape of X_train:', X_train.shape)
print('Shape of y_train:', y_train.shape)
print('Shape of X_test:', X_test.shape)
print('Shape of y_test:', y_test.shape)
print("Target Distribution (train):", y_train.value_counts())
print("Target Distribution (test):", y_test.value_counts())
#----------------------------------------------------------------------------------------------------------------------
# Training The Model
model = LogisticRegression()
model.fit(X_train, y_train)

#----------------------------------------------------------------------------------------------------------------------
# Evaluation
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)
cr = classification_report(y_test, y_pred, zero_division=0)
print("Classification Report:\n")
print(cr)
#----------------------------------------------------------------------------------------------------------------------
# Cross Validation
scores = cross_val_score(model, X_train, y_train, cv=5, scoring="accuracy")
recall = cross_val_score(model, X_train, y_train, cv=5, scoring='recall')

avg_scores = scores.mean()
std_dev = scores.std()
avg_recall = recall.mean()

print(f"5-fold CV Scores: {scores}")
print(f"The Avg of 5-Fold CV Scores: {avg_scores}")
print(f"The Std Dev of 5-Fold CV Scores: {std_dev}")
print(f"Recall of 5-Fold CV Scores: {recall}")
print(f"The Avg Recall Score: {avg_recall}")
#----------------------------------------------------------------------------------------------------------------------
# Inspecting Model Coefficients
coefficients = model.coef_[0]
print("Coefficients:")
print(coefficients)

# DataFrame Of Features Corresponding To Their Coefficients
features_df = pd.DataFrame(
    zip(X_train.columns, coefficients),
    columns=["feature", "coefficient"]
)

# Sorting Values In Descending Order
features_df = features_df.sort_values(by="coefficient", ascending=False)
print(features_df)

print("\n** MODEL INSIGHTS **\n")
print("Top Positive Predictor:")
print(features_df.iloc[0]["feature"])

print("\nModerate Predictor:")
print(features_df.iloc[2]["feature"])
print("\nNegative Predictor:")
print(features_df.iloc[-1]["feature"])
#----------------------------------------------------------------------------------------------------------------------

print("\n** Final Model Summary **\n")

print("Test Accuracy: 0.67")
print("Cross Validation Accuracy: 0.83")
print("Cross Validation Std Dev: 0.21")

print("Strongest Positive Predictor: Age")
print("Strongest Negative Predictor: department_marketing")