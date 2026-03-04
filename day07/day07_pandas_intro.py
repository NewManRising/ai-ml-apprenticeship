# Imported Library
import pandas as pd
#--------------------------------------------------------------------------

# Loading data
data = pd.read_csv("day07_data.csv")

# Making a copy
df = data.copy()

# General information and the dataframe
print(df)
print(df.shape)
print(df.columns.tolist())
print(df.head())
print(df.dtypes)

#-----------------------------------------------------------------------

# Printing values of selected columns
salary = df["salary"]
name_and_dept = df[["name", "department"]]

print(salary)
print(name_and_dept)

# Printing basic aggregation of data
avg_age = df["age"].mean()
avg_salary = df["salary"].mean()
print(round(avg_age))
print(round(avg_salary))
#-----------------------------------------------------------------------

# Boolean filtering
salary_50k = df[df["salary"] > 50000]
age_30 = df[df["age"] > 30]
only_sales = df[df["department"] == "Sales"]
sales_50k = df[(df["salary"] > 50000) & (df["department"] == "Sales")]

print("\nSalaries over 50K:\n\n", salary_50k)
print("\nAge over 30:\n\n", age_30)
print("\nOnly the sales department:\n\n", only_sales)
print("\nSalaries over 50k in sales department:\n\n", sales_50k)

#---------------------------------------------------------------------------

# Creating new column
df["high_earner"] = df["salary"] > 60000
num_high_earners = df["high_earner"].sum()
print("\n# of High Earners:\n\n", num_high_earners)

# Saving new dataframe
df.to_csv("day07_modified.csv", index=False)
print(df)