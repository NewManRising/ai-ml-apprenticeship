# Imports
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
#----------------------------------------------------------------------------------------------------------------------
# Loading Data
X = pd.read_csv("X_encoded.csv")
y = pd.read_csv("y.csv").squeeze()

y = y.map({"good": 0, "bad": 1})

print(y.head())

#----------------------------------------------------------------------------------------------------------------------
# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# Training Model
log_reg = LogisticRegression(max_iter=10000)

log_reg.fit(X_train, y_train)
#----------------------------------------------------------------------------------------------------------------------
# Predictions
y_pred = log_reg.predict(X_test)

# Evaluation
print("\nConfusion Matrix\n")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report\n")
print(classification_report(y_test, y_pred))