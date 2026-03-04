# Imports
import pandas as pd
#---------------------------------------------------------------------------------------------------------------------

# Loading Data
data = pd.read_csv("day08_messy_data.csv")
df = data.copy()

# Inspecting Data
row_before, column_before = df.shape
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.head(10))
#----------------------------------------------------------------------------------------------------------------------

# Checking Missing Values
missing = df.isna().sum()

print("\n*** MISSING VALUES REPORT ***\n")
for column, count in missing.items():
    print(column, count)

#----------------------------------------------------------------------------------------------------------------------

# Standardizing Text
df["department"] = df["department"].str.strip().str.capitalize()

# Converting Data Types and Filling Missing Values
df["salary"] = pd.to_numeric(df["salary"], errors='coerce')
df[["salary", "age"]] = df[["salary", "age"]].fillna(df[["salary", "age"]].median())

df["start_date"] = pd.to_datetime(df["start_date"]).fillna(pd.Timestamp('2021-03-21'))

# Data Cleaning Report
row_after, column_after = df.shape
missing_after = df.isna().sum()

print("*** DATA CLEANING REPORT ***\n")
print("Rows, Columns BEFORE:", (row_before, column_before))
print("Rows, Columns AFTER:", (row_after, column_after))
print("\nMissing Values BEFORE:\n\n")
print(missing)
print("\nMissing Values AFTER:\n\n")
print(missing_after)

print(df)
print(df.info())
# Saving Cleaned .csv
df.to_csv("day08_cleaned_data.csv", index=False)




