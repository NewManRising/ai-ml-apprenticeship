# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#----------------------------------------------------------------------------------------------------------------------
# Loading Data
data = pd.read_csv("day09_cleaned_data.csv")
df = data.copy()

#----------------------------------------------------------------------------------------------------------------------
# Inspecting Data
print(df.shape)
print(df.columns.tolist())
print(df.head())

# Calculating Statistics
print("\n** Individual Statistics For Age **\n")
print("Avg Age:", df["age"].mean())
print("Median Age:", df["age"].median())
print("Min Age:", df["age"].min())
print("Max Age:", df["age"].max())
print("Std of Age:", df["age"].std())

print("\n** Individual Statistics For Salary **\n")
print("Avg Salary:", df["salary"].mean())
print("Median Salary:", df["salary"].median())
print("Min Salary:", df["salary"].min())
print("Max Salary:", df["salary"].max())
print("Std of Salary:", df["salary"].std())

print("\n** Summary Statistics **\n")
print(df.describe())

#----------------------------------------------------------------------------------------------------------------------


# How many employees are in each department?
employees_per_dept = df.groupby("department").size().sort_values(ascending=False)
print("\n** Number of Employees per Department **\n")
print(employees_per_dept)


# What is the average salary per department?
avg_salary_per_dept = df.groupby("department")["salary"].mean().sort_values(ascending=False)
print("\n** Avg Salary Per Department **\n")
print(avg_salary_per_dept)


# What is the average age per department?
avg_age_per_dept = df.groupby("department")["age"].mean().sort_values(ascending=False)
print("\n** Avg Age Per Department **\n")
print(avg_age_per_dept)


# How many high earners exist?
df["high_earner"] = df["salary"] > 60000
high_earners = df["high_earner"].sum()
print("\n** Number of High Earners **\n")
print(high_earners)

# Which departments contain the most high earners?
high_earner_dept = df.groupby("department")["high_earner"].sum()
print("\n** Number of High Earners by Department **\n")
print(high_earner_dept)

# Saving Modified DataFrame
df.to_csv("day09_cleaned_data_modified.csv", index=False)
#-------------------------------------------------------------------------------------


# Bar Chart of # Employees Per Department
plt.figure(figsize=(8, 6))
employees_per_dept.plot(kind='bar', title='Number of Employees per Department', xlabel='Department', ylabel='Num of Employees')
plt.xticks(rotation=90)
plt.savefig("../reports/employees_by_dept.png",
            dpi=150, bbox_inches='tight')
plt.show()

# Bar Chart of Avg Salary Per Department
plt.figure(figsize=(8, 6))
avg_salary_per_dept.plot(kind='bar', title='Avg Salary per Department', xlabel='Department', ylabel='Avg Salary')
plt.xticks(rotation=90)
plt.savefig("../reports/avg_salary_per_dept.png",
            dpi=150, bbox_inches='tight')
plt.show()



# Report
print("\n** EDA Insights **\n")

print("1. The Sales department has the most employees with 6, followed by Marketing with 5 and Engineering with 4.")

print("2. The Engineering department has the highest average salary at $70,625.")

print("3. There are a total of 9 high earners who make more than $60,000.")

print("4. Engineering contains the largest concentration of high earners with a total of 4.")