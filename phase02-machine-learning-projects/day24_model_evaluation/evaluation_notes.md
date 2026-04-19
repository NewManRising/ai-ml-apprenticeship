# Model Evaluation - Day 24

I took all the best parameters, added class weights, and used the best model to make predictions.

I did a train-test split and then evaluated the results on unseen data that was held out. 

---

## Dataset
- Samples: 1000
- Features: 21
- Target Distribution:
  - Good (0): 70%
  - Bad (1): 30%

## Model
- Random Forest (tuned with GridSearchCV)
- Class Weight: balanced


Here were the results from GridSearchCV:

```
Best Parameters: {'bootstrap': True, 'criterion': 'gini', 'max_depth': 5, 'min_samples_leaf': 5, 'min_samples_split': 2, 'n_estimators': 200}
Best F1 Score: 0.590249065836538
Best Estimator: RandomForestClassifier(class_weight='balanced', max_depth=5, min_samples_leaf=5,
                       n_estimators=200, random_state=42)
```


---

## Performance Metrics

### Accuracy

- 0.70

### ROC-AUC

- 0.78


### Classification Report
````
- Class 0:
  - Precision: 0.86
  - Recall: 0.68
  - F1 Score: 0.76
- Class 1:
  - Precision: 0.50
  - Recall: 0.75
  - F1 Score: 0.60
 ````

---

## Confusion Matrix
````
[[95, 45],
[15, 45]]
````
---

## Key Insights

- The model performs better at identifying risky customers (recall = 0.75)
- Still produces a high number of false positives (45)
- This indicates a tradeoff between sensitivity and precision

---

The model prioritizes catching risky customers (0.75 recall). In a business setting this may be useful in detecting fraud or credit risks. However, the model predicts a lot more False Positives as a tradeoff and this could lead to rejecting good customers. 



---

## Next Steps

- Tune classification threshold
- Improve precision-recall balance
- Explore feature importance