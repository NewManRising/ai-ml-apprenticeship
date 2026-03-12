# Imports
import pandas as pd
#----------------------------------------------------------------------------------------------------------------------

# Loading Data
data = pd.read_csv("german_credit_data.csv")
df = data.copy()


# Inspecting The Data
print("\nShape Of Data:")
print(df.shape)
print("\nColumn Names:")
print(df.columns)
print("\nData Types:")
print(df.dtypes)
print("\nThe First 5 Rows:")
print(df.head())
#----------------------------------------------------------------------------------------------------------------------

# Checking For Missing Values And Duplicated Rows
print("\nMissing Values:")
print(df.isna().sum())
print("\nDuplicated Rows:")
print(df.duplicated().sum())


# Cleaning Columns for Better Readability
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(r'[^0-9a-zA-Z]+', '_', regex=True)
    .str.strip('_')
)

# Dropping Irrelevant Columns
df.drop(columns=["unnamed_0"], inplace=True)

print(df.columns.tolist())

# Checking Target Variable Distribution
print("\nTarget Distribution:")
print(df["risk"].value_counts())

# Summary Statistics
print("\n Summary Statistics:")
print(df.describe())