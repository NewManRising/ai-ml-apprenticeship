# Imports
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
#---------------------------------------------------------------------------------------------------------------------
# Loading Data
data = pd.read_csv("day11_cleaned_data.csv")
df = data.copy()
print(df.shape)
print(df.dtypes)
print(df.head(3))

#---------------------------------------------------------------------------------------------------------------------
# Creating New Date Columns
df["start_date"] = pd.to_datetime(df["start_date"])
df["start_year"] = df["start_date"].dt.year
df["start_month"] = df["start_date"].dt.month

#--------------------------------------------------------------------------------------------------------------------
# Defining Features and Target Variables
df["high_earner"] = df["salary"] > 60000

# Separating Features
X = df.drop(columns=["salary", "high_earner", "name", "start_date"])
y = df["high_earner"]

#---------------------------------------------------------------------------------------------------------------------

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

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))