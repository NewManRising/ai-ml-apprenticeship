This README is documenting and reinforcing concepts learned. 

1) What is a DataFrame?
A dataframe is a data structure in Pandas. It takes files like csv and xlsx and presents the data in a table containing rows and columns. It is a two-dimensional data structure that allows data manipulation, filtering, aggregation, and transformation in memory.

2) What does df. shape tell you?
df.shape gives you the shape of the dataframe. Ex: (3000, 10). This tells you how many rows and columns exist in the dataset (row, column).

3) What is boolean filtering used for?
Boolean filtering allows you to filter through rows using a conditional operation. Only rows that match the condition are visible. Ex: df["sales"] > 50000. It evaluates a condition for each row and returns only the rows where the condition is True.

4) What does creating a derived column accomplish? It allows you to gain more insights from your dataset. It helps you to generate new features from existing data, which can reveal patterns, enable categorization, or prepare data for analysis and machine learning.

5) Why should you save a modified CSV?
It helps preserve the original data because you now have two copies. The modified version has saved all the changes you have made to the original dataset. It is a way have persistence with your data versus data being stored in memory. It separates raw data from processed data and ensures reproducibility.


“Day 6 — Pandas Practice”
Include:

I created a csv file to practice basic tasks with Pandas. I loaded the dataset into a dataframe, inspected it, and printed values of selected columns. I then filtered rows using boolean filtering and created a new column. Finally, I printed these values and saved the modified csv. These skills are essential and foundational to data science and preparing data for machine learning. 

