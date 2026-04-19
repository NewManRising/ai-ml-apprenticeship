# Imports
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
#----------------------------------------------------------------------------------------------------------------------
# Loading Data


# Loading Data
X = pd.read_csv("X_encoded.csv")
y = pd.read_csv("y.csv").squeeze()

y = y.map({"good": 0, "bad": 1})

print("\n** DATA INFO **")
print("X shape:", X.shape)
print("y shape:", y.shape)
print("\nTarget Distribution:\n", y.value_counts())
#----------------------------------------------------------------------------------------------------------------------
# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print('\n** TRAIN-TEST SPLIT **')
print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)
print("Train shape:", y_train.shape)
print("Test shape:", y_test.shape)

#Training Model
tree = DecisionTreeClassifier(random_state=42)
tree.fit(X_train, y_train)
#---------------------------------------------------------------------------------------------------------------------
# Predictions and Metrics
train_y_pred = tree.predict(X_train)
test_y_pred = tree.predict(X_test)

# Overfitting Check
print("\n** DECISION TREE RESULTS **")
print("Training Accuracy:")
print(accuracy_score(y_train, train_y_pred))
print("Testing Accuracy:")
print(accuracy_score(y_test, test_y_pred))

# Metrics
print("\nClassification Report:\n")
print(classification_report(y_test, test_y_pred))
print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, test_y_pred))