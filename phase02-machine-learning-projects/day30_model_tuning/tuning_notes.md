# Day 30 — Model Tuning

## Objective
Tune the top two candidate models and compare them fairly.

## Models Tuned
- Logistic Regression
- Random Forest

## Best Parameters
```
Tuned Logistic Regression
Best Params: {'model__C': 1, 'model__solver': 'liblinear'}
```
```
Tuned Random Forest
Best Params: {'model__max_depth': 2, 'model__min_samples_leaf': 3, 'model__n_estimators': 300}
```
## Results
```
                       model                                                                        best_params  cv_best_f1  precision_1  recall_1      f1_1  accuracy
1        Tuned Random Forest  {'model__max_depth': 2, 'model__min_samples_leaf': 3, 'model__n_estimators': 300}    0.584473     0.484211  0.766667  0.593548     0.685
0  Tuned Logistic Regression                                      {'model__C': 1, 'model__solver': 'liblinear'}    0.588564     0.500000  0.716667  0.589041     0.700
```

Tuned Random Forest confusion matrix:
```
[[91 49]
 [14 46]]
 ```
Tuned Logistic Regression confusion matrix:
```
[[97 43]
 [17 43]]
 ```

## Winner
The tuned Logistic Regression model is the winner here. Recall for the minority class was higher with Random Firest at 0.77, compared to 0.72 ( log reg).


However, Their F1 scores are very close. Random Forest 0.593. Logistic Regression 0.589.

Looking at the confusion matrices of each tuned model, Random Forest had fewer False Negatives. But still very close.

After tuning both Logistic Regression and Random Forest, performance was nearly identical on minority-class F1. I selected Logistic Regression because it achieved comparable results with lower complexity and better interpretability.

## Key Insight
Data is not complex and relationships are mostly linear. Using Random Forest in this situation adds unnecessary complexity. Logistic Regression wins due to simplicity, stableness, and easier interpretability. 