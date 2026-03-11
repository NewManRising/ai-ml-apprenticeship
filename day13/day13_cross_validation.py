# Imports
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
#---------------------------------------------------------------------------------------------------------------------
# Loading Data
data = pd.read_csv("day13_cleaned_data.csv")
df = data.copy()
print(df.shape)
print(df.dtypes)
print(df.head(3))


#---------------------------------------------------------------------------------------------------------------------

# Separating Features
X = df.drop(columns=["salary", "high_earner", "name", "start_date"])
y = df["high_earner"]


# Encoding Dept Column
encoded_dept = pd.get_dummies(X, columns=["department"], drop_first=True)
X = encoded_dept
print("New Shape:\n", X.shape)
print("Feature Columns:\n", X.columns.tolist())

#---------------------------------------------------------------------------------------------------------------------

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

#----------------------------------------------------------------------------------------------------------------------
print("\n** Final Report **\n")
print("Original Dataset Shape:", df.shape)
print("Feature Table Shape:", X.shape)
print("Train Dataset Shape:", X_train.shape)
print("Test Dataset Shape:", X_test.shape)
print("\nTarget Distribution (train):\n", y_train.value_counts())
print("\nTest Distribution (test):\n", y_test.value_counts())

#---------------------------------------------------------------------------------------------------------------------
# Building Logistic Regression Model
model = LogisticRegression()
model.fit(X_train, y_train)

#---------------------------------------------------------------------------------------------------------------------
# Metrics and Evaluation
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

#---------------------------------------------------------------------------------------------------------------------
# Implementing Cross-Validation
scores = cross_val_score(model, X, y, cv=5)
recall = cross_val_score(model, X, y, cv=5, scoring="recall")


avg_scores = scores.mean()
Std_dev = scores.std()
avg_recall = recall.mean()

print("\nAccuracy of CV:")
print(scores)
print("\nAvg Accuracy Score of CV:")
print(avg_scores)
print("\nStd Dev of CV:")
print(Std_dev)

print("\nRecall Score of CV:")
print(recall)
print("\nAvg Recall Score of CV:")
print(avg_recall)
