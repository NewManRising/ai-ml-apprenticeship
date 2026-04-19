# Imports
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
#---------------------------------------------------------------------------------------------------------------------
# Loading Data
X = pd.read_csv("X_encoded.csv")
y = pd.read_csv("y.csv").squeeze()

# Mapping Binary Values To Labels
y = y.map({"good": 0, "bad": 1})

print("\n** DATA INFO **")
print("\nShape Of X:", X.shape)
print("Shape Of y:", y.shape)
print("\nTarget Distribution:\n", y.value_counts())
#---------------------------------------------------------------------------------------------------------------------
# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\n** TRAIN-TEST SPLIT **")
print("\nShape of X_train:", X_train.shape)
print("Shape Of X_test:", X_test.shape)
print("Shape Of y_train:", y_train.shape)
print("Shape Of y_test:", y_test.shape)
#---------------------------------------------------------------------------------------------------------------------
# Training Model
forest = RandomForestClassifier(
    random_state=42,
    n_estimators=100
)

forest.fit(X_train, y_train)
#---------------------------------------------------------------------------------------------------------------------
# Predictions And Evaluation
y_pred_train = forest.predict(X_train)
y_pred_test = forest.predict(X_test)

print("\n** RANDOM FOREST EVALUATION **")
print("\nTraining Accuracy:", accuracy_score(y_train, y_pred_train))
print("Test Accuracy:", accuracy_score(y_test, y_pred_test))
print("\nClassification Report:\n\n", classification_report(y_test, y_pred_test, zero_division=0))
print("Confusion Matrix:\n\n", confusion_matrix(y_test, y_pred_test))

