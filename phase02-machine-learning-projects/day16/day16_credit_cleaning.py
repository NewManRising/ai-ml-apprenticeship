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

# Summary Statistics
print("\n Summary Statistics:")
print(df.describe())

# Checking Target Variable Distribution
print("\nTarget Distribution:")
print(df["risk"].value_counts())
print("\nUnique Values:")
print(df["risk"].unique())


# Checking For Missing Values And Duplicated Rows
print("\nMissing Values:\n")
print(df.isna().sum())
print("\nDuplicated Rows:")
print(df.duplicated().sum())


for col in df.columns:
    unique_vals = df[col].unique()
    if len(unique_vals) < 20:
        print(f"\nColumn: {col}")
        print(unique_vals)


df[["checking_account", "saving_accounts"]] = df[["checking_account", "saving_accounts"]].fillna('unknown')

print("\nMissing Values:\n")
print(df.isna().sum())

df.to_csv("day16_cleaned_credit_data.csv")