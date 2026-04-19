# Day 29 — Model Comparison

## Objective
Compare multiple models using the same pipeline and engineered features.

## Models Tested
- Logistic Regression
- Random Forest
- Gradient Boosting

## Results
I printed a classification report and confusion matrix for each model. Addtionally, I created a comparison table to compare their performance on the minority class (class 1).

Below is the printed results:
```
LogisticRegression
              precision    recall  f1-score   support

           0       0.85      0.69      0.76       140
           1       0.50      0.72      0.59        60

    accuracy                           0.70       200
   macro avg       0.68      0.70      0.68       200
weighted avg       0.75      0.70      0.71       200

[[97 43]
 [17 43]]
 ```
```

RandomForest
              precision    recall  f1-score   support

           0       0.78      0.87      0.82       140
           1       0.58      0.42      0.49        60

    accuracy                           0.73       200
   macro avg       0.68      0.64      0.65       200
weighted avg       0.72      0.73      0.72       200

[[122  18]
 [ 35  25]]
 ```
```
GradientBoosting
              precision    recall  f1-score   support

           0       0.80      0.86      0.83       140
           1       0.60      0.50      0.55        60

    accuracy                           0.75       200
   macro avg       0.70      0.68      0.69       200
weighted avg       0.74      0.75      0.74       200

[[120  20]
 [ 30  30]]
 ```
And here is the comparison table for the minority class:
```

*** Comparison Table For All Models On Minority Class ***

                model  precision_1  recall_1      f1_1  accuracy
0  LogisticRegression     0.500000  0.716667  0.589041     0.700
2    GradientBoosting     0.600000  0.500000  0.545455     0.750
1        RandomForest     0.581395  0.416667  0.485437     0.735
```



## Best Model
Logistic regression is the best performer here. It contains the highest recall (0.72) and F1 score (0.59).

## Key Insight
It seems the simpler model (log reg) does best with this data. The reason being is that features are limited, relationships are simple, and the data is not highly nonlinear. The more complex models just perform weaker given these conditions. 

Next, I will hypertune logistic regression and random forest and compare. 