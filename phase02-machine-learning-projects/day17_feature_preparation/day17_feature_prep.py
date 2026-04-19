# Imports
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
#----------------------------------------------------------------------------------------------------------------------
# Loading Data
data = pd.read_csv("day17_cleaned_credit_data.csv")
df = data.copy()

# Inspecting Data
print("Shape Of DF:\n", df.shape)
print("\nColumn Names:\n", df.columns.tolist())
print("\nFirst 3 Rows:\n", df.head(3))
#----------------------------------------------------------------------------------------------------------------------
# Defining Features And Target Variables
X = df.drop(columns=["risk"])
y = df["risk"]
print("Shape of X:\n", X.shape)
print("Shape of y:\n", y.shape)
#----------------------------------------------------------------------------------------------------------------------
# Identifying Categorical And Numerical Columns
cat_columns = df.select_dtypes(include="object").columns.tolist()
num_columns = df.select_dtypes(include="number").columns.tolist()
print("Categorical Columns:\n", cat_columns)
print("Numerical Columns:\n", num_columns)
#----------------------------------------------------------------------------------------------------------------------
# Encoding Categorical Features
X = pd.get_dummies(X, drop_first=True)
print("Encoded Shape of X:\n", X.shape)
print("Encoded Columns Of X:\n", X.columns.tolist())
print("Encoded First 5 Rows:\n", X.head(5))

# Saving Data
X.to_csv("X_encoded.csv", index=False)
y.to_csv("y.csv", index=False)
