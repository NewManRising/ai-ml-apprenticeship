## Employee Salary Prediction Model

The purpose of this model was to predict high income earners based on demographics and employment features.

I started with 15 samples and 5 columns (name, age, dept, salary, and start date). I then created columns for start month, start year, and high earner. High earners are those with salaries greater than $60,000.

The process I followed was:
* Loading in the data
* Inspecting data
* Engineering new features
* Defining feature table and target variable
* Encoding categorical columns (Department)
* Train-test split
* Training a logistic regression model and evaluation
* Cross Validation 
* Model coefficient interpretation

#### Metrics received

Test Accuracy: 0.67

Cross Validation Mean Accuracy: 0.83

Cross Validation Std Dev: 0.21

Recall Score: 1.00

The highest positive predictor was age. The strongest negative predictor was department_marketing.

The biggest limitation was the size of the dataset. With 15 rows or samples, there was not a lot for the model to learn from. Due to the small size, the model is more likely to make a mistake that has a big impact on the final results. 

Cross validation achieved an average accuracy of 0.83, which is better than the single train-test split. However, standard deviation was 0.21. Which means the model is unstable due to the small dataset it's working with.

In the future, using a dataset that is larger would help remedy this problem. Additionally, trying other models and using different pipelines would help out. 