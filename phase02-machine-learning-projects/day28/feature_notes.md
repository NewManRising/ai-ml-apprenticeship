# Day 28 — Feature Engineering

## Objective
Improve model performance by creating new features.

## Features Added
- credit_group
- purpose_credit_interaction
- housing_savings

## Results
Here are the results of the pipeline with engineered features.
```

Classification Report: 
               precision    recall  f1-score   support

           0       0.87      0.65      0.74       140
           1       0.48      0.77      0.59        60

    accuracy                           0.69       200
   macro avg       0.68      0.71      0.67       200
weighted avg       0.75      0.69      0.70       200

Confusion Matrix:
 [[91 49]
 [14 46]]
```
And here is the pipeline run without the engineered features.
```
Classification Report: 
               precision    recall  f1-score   support

           0       0.85      0.70      0.77       140
           1       0.51      0.72      0.59        60

    accuracy                           0.70       200
   macro avg       0.68      0.71      0.68       200
weighted avg       0.75      0.70      0.72       200

Confusion Matrix:
 [[98 42]
 [17 43]]
 ```
## Key Insight
Based on the above information, the engineered features made some tiny improvements in recall for the minority class. While it is a step in the right direction the engineered features are not very strong signals. 
## Next Step
I will refine or remove weak features and test again. 